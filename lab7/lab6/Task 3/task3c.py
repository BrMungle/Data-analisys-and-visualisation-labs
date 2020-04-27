import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pathlib

temperatures = pd.read_csv('data/temperatures_clean.csv')

countries = list(set(list(temperatures['country_id'])))
avg_temperatures = []
for x in countries:
    avg_temperatures.append(list(temperatures.loc[temperatures['country_id'] == x]['AverageTemperatureCelsius']))
            

fig, ax = plt.subplots(figsize = [7,5], dpi = 150)

ax.violinplot(dataset = avg_temperatures,positions = list(range(len(countries))))
ax.set_xticklabels(countries)
ax.grid(True)

if(len(sys.argv) > 1):
    if sys.argv[1] == '1':
        fig.savefig('plots/task3c.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task3c.png')
    elif sys.argv[1] == '0':
        plt.show()
