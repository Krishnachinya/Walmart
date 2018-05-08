import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

dataModel = pd.read_csv('linear_model.csv')
dataTrain = pd.read_csv('train.csv')

data2012=pd.DataFrame();
data2013=pd.DataFrame();


dataModel['Dates'] = pd.to_datetime(dataModel['Dates'])
# Convert to datetime object
dataModel['Dates'] = pd.to_datetime(dataModel['Dates'],format='%Y%m%d')
dataModel = dataModel[dataModel['Dates'].dt.year > 2011]


dataTrain['Date'] = pd.to_datetime(dataTrain['Date'])
# Convert to datetime object
dataTrain['Date'] = pd.to_datetime(dataTrain['Date'],format='%Y%m%d')
dataTrain = dataTrain[dataTrain['Date'].dt.year > 2011]


# For 2012 - sales
data2012 = dataTrain[(dataTrain['Date'] > '2011-11-11') & (dataTrain['Date'] < '2012-09-01')]
# for prediction
data2013 = dataModel[(dataModel['Dates'] > '2012-09-02') & (dataModel['Dates'] < '2013-07-26')]

data2012 = data2012[data2012['Store'] == 1]
data2013 = data2013[data2013['Store'] == 1]

data2012 = data2012[data2012['Dept'] == 1]
data2013 = data2013[data2013['Dept'] == 1]

plt.plot(data2012['Date'], data2012['Weekly_Sales'])
plt.show();

plt.plot(data2013['Dates'], data2013['Weekly_Sales'])
plt.show();
