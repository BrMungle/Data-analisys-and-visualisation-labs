import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

populations = pd.read_csv('data/Populations.csv')
codes = pd.read_csv('data/country_codes.csv')

def help_func_1 (v):
    return(v[2:5])
    
codes['Alpha-3 code'] = list(map(help_func_1,codes['Alpha-3 code']))
populations = populations.loc[populations['Country Code'].isin(list(codes['Alpha-3 code']))]

years = list(map(str,list(range(1960,2019))))
selected_year = years[int(np.random.choice(len(years),1))]

table_temp = populations[['Country Name', str(selected_year)]]
table_temp.sort_values(by = str(selected_year), ascending = False, inplace = True)

index_PL = list(table_temp['Country Name']).index('Poland')
table_temp = table_temp.iloc[range(index_PL - 2, index_PL + 3)]

#making a bar plot
fig, ax = plt.subplots(figsize = [5,5], dpi = 100)
labels = table_temp['Country Name']
x = np.arange(len(labels))
y = table_temp[selected_year]
    
ax.bar(x,y)
ax.set_ylabel('Population')
ax.set_xlabel('Country')
ax.set_title('Population in Poland and 4 closest \n countries by population in ' + str(selected_year))
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.xticks(rotation=30)
fig.subplots_adjust(bottom=0.3)
fig.savefig('plots/plot_task_c.png')
plt.show()

    




