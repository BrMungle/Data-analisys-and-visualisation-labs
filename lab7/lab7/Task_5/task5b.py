import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pathlib

temperatures = pd.read_csv('data/temperatures_clean.csv')

country_mean_temperatures = np.zeros(len(temperatures.index))
city_mean_temperatures = np.zeros(len(temperatures.index))

for year in list(set(temperatures['year'])):
    for country in list(set(temperatures['Country'])):
        for city in list(set(temperatures['City'].loc[temperatures['Country'] == country])):
            indexes = (temperatures['year'] == year) & (temperatures['Country'] == country) & (temperatures['City'] == city)
            mean_temp = np.mean(temperatures['AverageTemperatureCelsius'].loc[indexes])
            city_mean_temperatures[indexes] = mean_temp
        indexes = (temperatures['year'] == year) & (temperatures['Country'] == country)
        mean_temp = np.mean(temperatures['AverageTemperatureCelsius'].loc[indexes])
        country_mean_temperatures[indexes] = mean_temp
        
temperatures['avg_temperature_in_year'] = country_mean_temperatures
temperatures['avg_temperature_in_year_by_city'] = city_mean_temperatures

temperatures.sort_values(inplace = True, by = 'year')
min_year = min(temperatures['year'])
max_year = max(temperatures['year'])
min_temperature = min(temperatures['avg_temperature_in_year_by_city'])
max_temperature = max(temperatures['avg_temperature_in_year_by_city'])

colors = ['gray','red','gold','royalblue','plum','k','lightblue','yellow']
fig, axs = plt.subplots(3, 3,figsize = [10,5], dpi = 150)

row = 0
column = 0
i = 0
for country in list(set(temperatures['Country'])):
    country_table_temp = temperatures.loc[temperatures['Country'] == country]
    is_labeled = False
    for city in list(set(country_table_temp['City'])):
        table_temp = country_table_temp.loc[country_table_temp['City'] == city]
        if(not is_labeled):
            axs[row,column].plot(table_temp['year'], table_temp['avg_temperature_in_year_by_city'],label=country, linestyle = '-', color = colors[i], linewidth = 0.5)
        else:
            axs[row,column].plot(table_temp['year'], table_temp['avg_temperature_in_year_by_city'],linestyle = '-', color = colors[i], linewidth = 0.5)
        is_labeled = True
        
    axs[row,column].set_title(country)
    axs[row,column].set_xlim(min_year,max_year)
    axs[row,column].set_ylim(min_temperature -5,max_temperature + 5)
  
    column = column + 1
    i = i+1
    if(column == 3):
        column = 0
        row = row + 1

axs[row,column].axis('off')
plt.subplots_adjust(hspace=0.5)

fig.subplots_adjust(bottom=0.1, left = 0.1, right = 0.8)
leg = fig.legend(loc='center right')

for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0)

if(len(sys.argv) > 1):
    if sys.argv[1] == '1':
        fig.savefig('plots/task5b.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task5b.png')
    elif sys.argv[1] == '0':
        plt.show()  
