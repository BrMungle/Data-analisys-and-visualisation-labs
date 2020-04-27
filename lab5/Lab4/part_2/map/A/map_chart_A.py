import pandas as pd
import imageio
import pygal.maps.world
from pygal.style import Style 

worldmap_chart = pygal.maps.world.World()


populations = pd.read_csv('data/Populations.csv')
codes = pd.read_csv('data/country_codes.csv')

def help_func_1 (v):
    return(v[2:5])
    
def help_func_2 (v):
    return(v[2:4])
        
codes['Alpha-3 code'] = list(map(help_func_1,codes['Alpha-3 code']))
populations = populations.loc[populations['Country Code'].isin(list(codes['Alpha-3 code']))]
populations.sort_values(by = 'Country Name', inplace = True)

codes['Alpha-2 code'] = list(map(help_func_2,codes['Alpha-2 code']))
codes['Alpha-2 code'] = list(map(lambda x: x.lower(),codes['Alpha-2 code']))
years = list(map(str,list(range(1960,2019))))

table_temp = codes[['Alpha-2 code','Alpha-3 code']]
populations = populations.merge(right = table_temp, left_on = 'Country Code', right_on = 'Alpha-3 code')
populations.drop_duplicates(inplace = True)


def help_func_3(x):
    y = str(int(x+100))
    while(len(y) != 3):
        y = '0' + y
    return(y)
    
images = []
for year in years[1:]:
    #year = years[1]
    table_temp = populations[['Country Name','Country Code','Alpha-2 code', year]]
    table_temp.sort_values(by = year, ascending = False, inplace = True)
    table_temp = table_temp.iloc[list(range(5))]
    table_temp.sort_values(by = year, ascending = True, inplace = True)
    colors_temp = []
    for i in range(5):
        population_temp = help_func_3(round(list(table_temp[year])[i]/(10**7),0))
        blue_temp = help_func_3(100 -round(list(table_temp[year])[i]/(10**7),0))
        colors_temp.append('#' +'{0:02X}'.format(int(population_temp))+'{0:02X}'.format(25)+'{0:02X}'.format(int(blue_temp)))
    print(colors_temp)
    
    new_style = Style(colors=colors_temp)

    
    worldmap_chart = pygal.maps.world.World(legend_at_bottom=True, 
                                            legend_at_bottom_columns=5,
                                            height=900,
                                            width=1600,
                                            style = new_style
                                            )
    worldmap_chart.title = '5 most populated countries in ' + year
    
    for i in range(5):
        population_temp =': ' + str(round(list(table_temp[year])[i]/(10**9),1)) + ' B'
        #value_temp = round(list(table_temp[year])[i]/(10**9),1)
        dict_temp = dict()
        dict_temp[list(table_temp['Alpha-2 code'])[i]] = population_temp
        worldmap_chart.add(list(table_temp['Country Name'])[i] + population_temp,dict_temp)
    
    worldmap_chart.render_to_png('plots/chart.png')
    images.append(imageio.imread('plots/chart.png'))

imageio.mimsave('plots/map_plot_A.gif', images)
 
