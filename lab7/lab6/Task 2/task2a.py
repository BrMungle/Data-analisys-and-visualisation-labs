import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pathlib

temperatures = pd.read_csv('data/temperatures_clean.csv')

#part a)
fig, ax = plt.subplots(figsize = [7,5], dpi = 150)

ax.scatter(x = temperatures['year'], y = temperatures['AverageTemperatureCelsius'], marker = 'o', facecolors='none', edgecolor = 'black')
ax.set_xlabel('Year')
ax.set_ylabel('Average temperature')

if(len(sys.argv) > 1):
    if sys.argv[1] == '1':
        fig.savefig('plots/task2a.png')
        print('Plot saved in: '+str(pathlib.Path().absolute()) + '/plots/task2a.png')
    elif sys.argv[1] == '0':
        plt.show()


        

