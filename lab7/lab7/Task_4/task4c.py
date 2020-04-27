import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pathlib

temperatures = pd.read_csv('data/temperatures_clean.csv')

mean_temperatures = np.zeros(len(temperatures.index))

for year in list(set(temperatures['year'])):
    for country in list(set(temperatures['Country'])):
        indexes = (temperatures['year'] == year) & (temperatures['Country'] == country)
        mean_temp = np.mean(temperatures['AverageTemperatureCelsius'].loc[indexes])
        mean_temperatures[indexes] = mean_temp
        
temperatures['avg_temperature_in_year'] = mean_temperatures
temperatures.sort_values(inplace = True, by = 'year')

fig, ax = plt.subplots(figsize = [10,5], dpi = 150)

for country in list(set(temperatures['Country'])):
    table_temp = temperatures.loc[temperatures['Country'] == country]
    ax.plot(table_temp['year'], table_temp['avg_temperature_in_year'],label=country, alpha = 0.7)

fig.subplots_adjust(bottom=0.1, left = 0.1, right = 0.8)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('Year')
ax.set_ylabel('Average temperature')   

if(len(sys.argv) > 1):
    if sys.argv[1] == '1':
        fig.savefig('plots/task4c.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task4c.png')
    elif sys.argv[1] == '0':
        plt.show()
  
