import pandas as pd
import numpy as np
import matplotlib
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

images = []
for year in years:
    table_temp = populations[['Country Name', year]]
    table_temp.sort_values(by = year, ascending = False, inplace = True)
    table_temp = table_temp.iloc[list(range(5))]
    
    #making a bar plot
    fig, ax = plt.subplots(figsize = [5,5], dpi = 100)
    labels = table_temp['Country Name']
    x = np.arange(len(labels))
    y = table_temp[year]
    
    ax.bar(x,y)
    ax.set_ylabel('Population')
    ax.set_xlabel('Country')
    ax.set_title('5 most populated countries in ' + year)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=30)
    fig.subplots_adjust(bottom=0.3)
    fig.savefig('plots/Populations_in_' + year +'.png')
    plt.show()
    
    images.append(imageio.imread('plots/Populations_in_' + year +'.png'))

imageio.mimsave('plots/Task_a_animation.gif', images)
  

    




