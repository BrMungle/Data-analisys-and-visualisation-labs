import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio

populations = pd.read_csv('data/Populations.csv')
codes = pd.read_csv('data/country_codes.csv')

def help_func_1 (v):
    return(v[2:5])
    
codes['Alpha-3 code'] = list(map(help_func_1,codes['Alpha-3 code']))
populations = populations.loc[populations['Country Code'].isin(list(codes['Alpha-3 code']))]
populations.sort_values(by = 'Country Name', inplace = True)
years = list(map(str,list(range(1960,2019))))


countries = ['Iraq', 'Jordan', 'Lebanon', 'Syrian Arab Republic', 'Turkey', 'Israel']

table_temp = populations.loc[populations['Country Name'].isin(countries)]
biggest_population = max(list(table_temp[years].max()))
biggest_population = round(biggest_population/(10**6),1) * 10**6
jump = biggest_population / 4

y_ticks = [0]
y_labels = ['0']

for i in range(4):
    y_ticks.append(jump *(i+1))
    y_labels.append(str(round(jump *(i+1)/(10**6),2)) + 'M')




    
#in colors
images = []
for year in years:
    #year = '2012'
    if int(year) < 2011: 
        table_temp = populations[['Country Name','Country Code', year]]
        table_temp = table_temp.loc[table_temp['Country Name'].isin(countries)]
        table_temp['Country Name'].loc[table_temp['Country Name'] == 'Syrian Arab Republic'] = 'Syria'
        table_temp.sort_values(inplace = True, by = 'Country Name')
        
        #making a bar plot
        fig, ax = plt.subplots(figsize = [7,5], dpi = 150)
        labels = table_temp['Country Name']
        x = np.arange(len(labels))
        y = list(table_temp[year])
        
        #ax.bar(x,y)
        ax.set_ylabel('Population')
        ax.set_xlabel('Country')
        ax.set_title('Populations of the chosen\n countries in ' + year, pad = 20)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_labels)
        ax.set_ylim(0,biggest_population * 1.25)
        ax.set_xlim(x[0] - 1, x[len(x) -1] + 1)
        
        counter = 0
        for bar in ax.bar(x,y):
            ax.annotate(list(table_temp['Country Code'])[counter],
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center',
                        fontsize = 20,
                        fontweight = 'bold',
                        color = 'red')
            counter = counter +1
        
        plt.xticks(rotation=30)
        fig.subplots_adjust(bottom=0.3, top =0.75, left = 0.2, right = 0.8)
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
    else:
        table_temp = populations[['Country Name','Country Code', year]]
        table_temp = table_temp.loc[table_temp['Country Name'].isin(countries)]
        table_temp['Country Name'].loc[table_temp['Country Name'] == 'Syrian Arab Republic'] = 'Syria'
        table_temp.sort_values(inplace = True, by = 'Country Name')
        
        #making a bar plot
        fig, ax = plt.subplots(figsize = [7,5], dpi = 150)
        labels = table_temp['Country Name']
        x = np.arange(len(labels))
        y = list(table_temp[year])
        
        #ax.bar(x,y)
        ax.set_ylabel('Population')
        ax.set_xlabel('Country')
        ax.set_title('Populations of the chosen\n countries in ' + year, pad = 20)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_labels)
        ax.set_ylim(0,biggest_population * 1.25)
        ax.set_xlim(x[0] - 1, x[len(x) -1] + 1)
        
        
        
        counter = 0
        for bar in ax.bar(x,y):
            ax.annotate(list(table_temp['Country Code'])[counter],
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center',
                        fontsize = 20,
                        fontweight = 'bold',
                        color = 'red')
            counter = counter +1
            if counter == 4:
                war_coords = (bar.get_x() + bar.get_width() / 2, bar.get_height())
                print(war_coords)
        
        ax.annotate("WAR",
                    xy=(2.5,40*10**6),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    fontsize = 100,
                    fontweight = 'bold',
                    color = 'dimgray',
                    alpha = 0.65
                    )
        
        plt.xticks(rotation=30)
        fig.subplots_adjust(bottom=0.3, top =0.75, left = 0.2, right = 0.8)
        #plt.rc('font', size=12)          # controls default text sizes
        plt.rc('axes', titlesize=25)     # fontsize of the axes title
        plt.rc('axes', labelsize=22)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=15)    # fontsize of the tick labels
        #plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        #plt.rc('figure', size=1)  # fontsize of the figure title
        fig.savefig('plots/Populations.png')#, bbox_inches = 'tight'
        plt.show()
        for i in range(15): 
            images.append(imageio.imread('plots/Populations.png'))
        

imageio.mimsave('plots/war_animation.gif', images)

