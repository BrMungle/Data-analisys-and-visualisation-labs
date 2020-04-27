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

ax.plot(temperatures['year'], temperatures['avg_temperature_in_year'],'k-')
ax.set_xlabel('Year')
ax.set_ylabel('Average temperature')   

if(len(sys.argv) > 1):
    if sys.argv[1] == '1':
        fig.savefig('plots/task4a.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task4a.png')
    elif sys.argv[1] == '0':
        plt.show()
