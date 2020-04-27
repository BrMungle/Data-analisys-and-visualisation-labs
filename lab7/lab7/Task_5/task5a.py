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
min_year = min(temperatures['year'])
max_year = max(temperatures['year'])
min_temperature = min(temperatures['avg_temperature_in_year'])
max_temperature = max(temperatures['avg_temperature_in_year'] )

colors = ['gray','red','gold','royalblue','plum','k','lightblue','yellow']
fig, axs = plt.subplots(3, 3,figsize = [10,5], dpi = 150)

row = 0
column = 0
i = 0

for country in list(set(temperatures['Country'])):
    table_temp = temperatures.loc[temperatures['Country'] == country]
    axs[row,column].plot(table_temp['year'], table_temp['avg_temperature_in_year'],label=country, linestyle = '-', color = colors[i], linewidth = 0.5)
    axs[row,column].set_title(country)
    axs[row,column].set_xlim(min_year,max_year)
    axs[row,column].set_ylim(min_temperature,max_temperature)

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
        fig.savefig('plots/task5a.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task5a.png')
    elif sys.argv[1] == '0':
        plt.show()   
