import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

schedule = pd.read_csv('data/schedule.csv')

def help_func_1(x):
    index = x.find('–')
    date_1 = x
    date_2 = x
    if(index > -1):
        date_1 = x[:index]
        date_2 = x[index + 2:]
    
    return(date_1,date_2)
    
dates = list(map(help_func_1,list(schedule['Date'])))
schedule['First day'] = list(map(lambda x: x[0],dates))
schedule['Last day'] = list(map(lambda x: x[1],dates))

schedule['First day'] = list(map(lambda x: datetime.datetime(int(x[6:10]),int(x[3:5]),int(x[:2])),schedule['First day']))
schedule['Last day'] = list(map(lambda x: datetime.datetime(int(x[6:10]),int(x[3:5]),int(x[:2])),schedule['Last day']))

def help_func_2(x,width):
    y = x
    x_length = len(x)
    n_jumps = int(x_length/width)
    for i in range(width,(n_jumps) * width, width):
        str_temp = x[i:i+width]
        ind_temp = str_temp.find(' ')
        if ind_temp > -1:
            y = y[:i+ind_temp] + '\n' + y[i+ind_temp + 1:]
    str_temp = x[n_jumps * width:]
    ind_temp = str_temp.find(' ')
    if ind_temp > -1 and n_jumps >0:
        y = y[:n_jumps * width + ind_temp] + '\n' + y[n_jumps * width + ind_temp +1:]
    return(y)

schedule['Event plot'] = list(map(lambda x: help_func_2(x,30),list(schedule['Event'])))

event_ids_list = []
event_ids = dict()
counter = 0
for i in schedule['Event']:
    if i not in event_ids:
        event_ids[i] = counter
        counter = counter +1
    event_ids_list.append(event_ids[i])
    
schedule['Event id'] = event_ids_list 
    


day_0 = schedule['First day'][0]
schedule['Begin'] = list(map(lambda x: int((x- day_0).days), schedule['First day']))
schedule['End'] = list(map(lambda x: int((x- day_0).days), schedule['Last day']))
schedule['Width'] = schedule['End'] - schedule['Begin'] 
schedule['Width'].loc[schedule['Width'] == 0] = 1
    
y_ticks = list(schedule['Event id'])
y_labels = list(schedule['Event plot'])

def add_month(sourcedate):
    if sourcedate.month + 1 == 13:
        return(datetime.datetime(sourcedate.year + 1, 1, 1))
    else:
        return(datetime.datetime(sourcedate.year, sourcedate.month + 1, 1))

x_ticks =[0]
x_labels = [datetime.datetime(2019,10,1)]

for i in range(1,12):
    x_labels.append(add_month(x_labels[i-1]))
    x_ticks.append(int((x_labels[i]-x_labels[i-1]).days) + x_ticks[i-1])

x_labels = [x.strftime('%d - %b - %Y') for x in x_labels]

   
fig, ax = plt.subplots(figsize = [9,16], dpi = 100)
#ax.plot(schedule['First day'],list(schedule['Event plot']))
#ax.set_y_ticks(range(len(list(schedule['Event plot']))))
#ax.plot(schedule['Begin'],schedule['Event id'])
for i in range(len(schedule['Begin'])):
    ax.broken_barh([(schedule['Begin'][i], schedule['Width'][i])], 
                    (schedule['Event id'][i] - 0.4, 0.8), facecolors =('tab:orange')) 

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=90)
fig.subplots_adjust(bottom=0.1, top = 0.99, left = 0.4, right = 0.99)
fig.savefig('plots/Gantt_chart.png')
