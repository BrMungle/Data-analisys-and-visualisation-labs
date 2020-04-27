import numpy as np
import pandas as pd

temperature = pd.read_csv('data/temperature.csv')
temperature =  temperature[temperature['City'].notna()]
temperature =  temperature[temperature['Country'].notna()]
temperature =  temperature[temperature['Country'].notna()]
temperature =  temperature[temperature['AverageTemperatureFahr'].notna()]
temperature =  temperature[temperature['AverageTemperatureUncertaintyFahr'].notna()]

temperature['AverageTemperatureCelsius'] = temperature['AverageTemperatureFahr'] - [32] * len(temperature['AverageTemperatureFahr'])
temperature['AverageTemperatureCelsius'] = [x/1.8 for x in temperature['AverageTemperatureCelsius']]

temperature['AverageTemperatureUncertaintyCelsius'] = temperature['AverageTemperatureUncertaintyFahr'] - [32] * len(temperature['AverageTemperatureUncertaintyFahr'])
temperature['AverageTemperatureUncertaintyCelsius'] = [x/1.8 for x in temperature['AverageTemperatureUncertaintyCelsius']]

temperature.drop(labels = 'day', axis = 1, inplace = True)
temperature.drop(labels = ['AverageTemperatureFahr','AverageTemperatureUncertaintyFahr']
                 , axis = 1, inplace = True)
 
temperature.to_csv('data/temperatures_clean.csv')
 
