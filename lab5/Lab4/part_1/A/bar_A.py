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
populations.head(5)
years = list(map(str,list(range(1960,2019))))

biggest_population = max(list(populations[years].max()))
biggest_population = round(biggest_population/(10**9),1) * 10**9
jump = biggest_population / 4

y_ticks = [0]
y_labels = ['0']

for i in range(4):
    y_ticks.append(jump *(i+1))
    y_labels.append(str(round(jump *(i+1)/(10**9),2)) + 'B')

#in colors
images = []
for year in years:
    year = years[10]
    table_temp = populations[['Country Name','Country Code', year]]
    table_temp.sort_values(by = year, ascending = False, inplace = True)
    table_temp = table_temp.iloc[list(range(5))]
    
    #making a bar plot
    fig, ax = plt.subplots(figsize = [7,5], dpi = 150)
    labels = table_temp['Country Name']
    x = np.arange(len(labels))
    y = list(table_temp[year])
    
    #ax.bar(x,y)
    ax.set_ylabel('Population')
    ax.set_xlabel('Country')
    ax.set_title('5 most populated countries in ' + year, pad = 20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_ylim(0,biggest_population * 1.2)
    
    counter = 0
    for bar in ax.bar(x,y):
        ax.annotate(list(table_temp['Country Code'])[counter],
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize = 20)
        counter = counter +1
    
    
    plt.xticks(rotation=30)
    fig.subplots_adjust(bottom=0.3, left = 0.2, right = 0.8)
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

imageio.mimsave('plots/bar_a_animation.gif', images)
  
# black and white
images = []
for year in years:
    #year = years[10]
    table_temp = populations[['Country Name','Country Code', year]]
    table_temp.sort_values(by = year, ascending = False, inplace = True)
    table_temp = table_temp.iloc[list(range(5))]
    
    #making a bar plot
    fig, ax = plt.subplots(figsize = [7,5], dpi = 150)
    labels = table_temp['Country Name']
    x = np.arange(len(labels))
    y = list(table_temp[year])
    
    #ax.bar(x,y)
    ax.set_ylabel('Population')
    ax.set_xlabel('Country')
    ax.set_title('5 most populated countries in ' + year, pad = 20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_ylim(0,biggest_population * 1.2)
    
    counter = 0
    for bar in ax.bar(x,y, color = 'white', edgecolor = 'black', linewidth = 5):
        ax.annotate(list(table_temp['Country Code'])[counter],
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize = 20)
        counter = counter +1
    
    
    plt.xticks(rotation=30)
    fig.subplots_adjust(bottom=0.3, left = 0.2, right = 0.8)
    #plt.rc('font', size=12)          # controls default text sizes
    plt.rc('axes', titlesize=25)     # fontsize of the axes title
    plt.rc('axes', labelsize=22)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=15)    # fontsize of the tick labels
    #plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    #plt.rc('figure', size=1)  # fontsize of the figure title
    fig.savefig('plots/BW_Populations.png')
    
    plt.show()
    
    images.append(imageio.imread('plots/BW_Populations.png'))

imageio.mimsave('plots/BW_bar_a_animation.gif', images)    




