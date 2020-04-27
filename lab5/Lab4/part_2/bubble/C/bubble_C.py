import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio

populations = pd.read_csv('data/Populations.csv')
codes = pd.read_csv('data/country_codes.csv')
areas = pd.read_csv('data/country_area.csv')

def help_func_1 (v):
    return(v[2:5])

def adjust_names(x):
    y = str(x)
    y = y.replace(' ','\n')
    return(y)
    
codes['Alpha-3 code'] = list(map(help_func_1,codes['Alpha-3 code']))
populations = populations.loc[populations['Country Code'].isin(list(codes['Alpha-3 code']))]
areas = areas.loc[areas['Country Code'].isin(list(codes['Alpha-3 code']))]

years = list(map(str,list(range(1960,2019))))
selected_year = years[int(np.random.choice(len(years),1))]

table_temp = populations[['Country Name', str(selected_year)]]
table_temp.sort_values(by = str(selected_year), ascending = False, inplace = True)

index_PL = list(table_temp['Country Name']).index('Poland')
table_temp = table_temp.iloc[range(index_PL - 2, index_PL + 3)]

countries = list(table_temp['Country Name'])
sorted_countries = sorted(countries)

permutation = []
for x in countries:
    permutation.append(sorted_countries.index(x))

#table_test = table_temp.sort_values(inplace = False, by = 'Country Name')
#table_test = table_test.iloc[permutation]

table_temp = populations.loc[populations['Country Name'].isin(countries)]
biggest_population = max(list(table_temp[years].max()))
biggest_population = round(biggest_population/(10**6),1) * 10**6
jump = biggest_population / 4

y_ticks = [0]
y_labels = ['0']

for i in range(4):
    y_ticks.append(jump *(i+1))
    y_labels.append(str(round(jump *(i+1)/(10**6),2)) + 'M')

x_ticks = []
x_labels = []
for i in range(0,len(years) - 1, 10):
    x_ticks.append(int(years[i]))
    x_labels.append(years[i])


for x in range(len(years)):
    print(years[:x +1])

table_temp = populations[['Country Name','Country Code', years[len(years) - 4]]]
table_temp = table_temp.loc[table_temp['Country Name'].isin(countries)]
c_by_name = table_temp.sort_values(inplace = False, by = 'Country Name')
c_by_population = table_temp.sort_values(inplace = False, by = years[len(years) - 4],ascending = True)

c_by_name = list(c_by_name['Country Name'])
c_by_population = list(c_by_population['Country Name'])

jump = biggest_population / 4
desired_heights = []
for x in c_by_name:
    print(x)
    desired_heights.append(c_by_population.index(x)*jump)

desired_heights = [biggest_population*1.1]
jump = biggest_population / 4
for i in range(1,5):
    desired_heights.append(desired_heights[0] - i*jump)

desired_x = list(range(2010,1969,-1)) 

 
names_to_plot = []
countries_to_plot = []
populations_to_plot = []
colors = ['darkred','yellow','deepskyblue','green','darkmagenta']


images = []
for year in years[1:]:
    #year = years[1]
    table_temp = populations[['Country Name','Country Code', year]]
    table_temp = table_temp.loc[table_temp['Country Name'].isin(countries)]
    table_temp.sort_values(inplace = True, by = 'Country Name')
    table_temp.columns = ['Country Name','Country Code', 'Population']
    
    areas_temp = areas[['Country Code', year]]
    areas_temp.columns = ['Country Code', 'Area']
    
    table_temp = table_temp.merge(areas_temp, on = 'Country Code')
    table_temp['Density'] = np.divide(list(table_temp['Population']),
                                      list(table_temp['Area']))
    
    table_temp['Country Name'] = list(map(adjust_names,list(table_temp['Country Name'])))
      
    #making a bar plot
    fig, ax = plt.subplots(figsize = [7,5], dpi = 150)
    #x = np.arange(len(labels))
    #y = list(table_temp[year])
    
    for i in range(5):
        x = int(year)
        y = table_temp['Population'][i]
        d = table_temp['Density'][i] * 2
        ax.scatter(x, y, c= colors[i],edgecolor = 'black', linewidth = 1
                ,alpha = 0.6
                ,s = d
                , label = table_temp['Country Name'][i])
        
        #x_push = -1 * ((x[len(x)-1] - x[0])/len(years) - 0.5)**3
        y_push = 150 * (desired_heights[i] - y)/biggest_population
        x_push = 50 * (desired_x[i] - x)/len(desired_x) 
        
        if(i%2 != 0): 
            x_push = x_push 
        else:
            x_push = x_push -60
            
        plt.annotate(table_temp['Country Code'][i], # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(x_push,y_push), # distance from text to points (x,y)
                     ha='center',
                     fontsize = 20,
                     fontweight = 'bold',
                     color = colors[i],
                     alpha = 0.5,
                     arrowprops=dict(arrowstyle="-", color = colors[i], alpha = 0.5, linewidth = 1.5))
    #plt.show()
    
    #ax.bar(x,y)
    ax.set_ylabel('Population')
    ax.set_xlabel('Year')
    ax.set_title('Populations of the chosen\n countries in ' + year, pad = 20)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_ylim(0,biggest_population * 1.25)
    ax.set_xlim(x_ticks[0], x_ticks[len(x_ticks) -1] + 10)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), labelspacing=2)
    
    #plt.xticks(rotation=30)
    fig.subplots_adjust(bottom=0.15, top = 0.8, left = 0.2, right = 0.8)
    #plt.rc('font', size=12)          # controls default text sizes
    plt.rc('axes', titlesize=25)     # fontsize of the axes title
    plt.rc('axes', labelsize=22)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=15)    # fontsize of the tick labels
    #plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    #plt.rc('figure', size=1)  # fontsize of the figure title
    fig.savefig('plots/Populations.png')#, bbox_inches = 'tight'
    plt.show()
    
    images.append(imageio.imread('plots/Populations.png'))

imageio.mimsave('plots/bubble_C_animation.gif', images)


