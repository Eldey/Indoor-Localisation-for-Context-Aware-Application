from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KernelDensity
from sklearn import preprocessing
import pandas as pd


client = MongoClient('localhost',27017)
lopy1Wifi = client.SMART.WiFi_Data_Lopy1
lopy2Wifi = client.SMART.WiFi_Data_Lopy2
lopy3Wifi = client.SMART.WiFi_Data_Lopy3
lopy4Wifi = client.SMART.WiFi_Data_Lopy4
lopy5Wifi = client.SMART.WiFi_Data_Lopy5
lopy6Wifi = client.SMART.WiFi_Data_Lopy6
rpi1Wifi = client.SMART.WiFi_Data_Rpi1

numNets1 = []
times1 = []
numNets2 = []
times2 = []
rssi1 = []
rssi2 = []

for item in lopy1Wifi.find({ '$and' : [{'Time': {'$gt': '20190227T000000'}}, {'Time': {'$lte': '20190228T000000'}}]}):
    numNets1.append(len(item['Networks']))
    
    pos = item['Networks'].index('TelstraD293DF') if 'TelstraD293DF' in item['Networks'] else None
    if pos != None:
        rssi1.append(item['Signal Strengths'][pos])
    time1 = item['Time'][9:]
    time1 = ':'.join(time1[i:i+2] for i in range(0, len(time1), 2))
    times1.append(time1)
#print(rssi1)
for item in lopy4Wifi.find({ '$and' : [{'Time': {'$gt': '20190227T000000'}}, {'Time': {'$lte': '20190228T000000'}}]}):
    numNets2.append(len(item['Networks']))
    pos = item['Networks'].index('TelstraD293DF') if 'TelstraD293DF' in item['Networks'] else None
    if pos != None:
        rssi2.append(item['Signal Strengths'][pos])
    time2 = item['Time'][9:]
    time2 = ':'.join(time2[i:i+2] for i in range(0, len(time2), 2))
    times2.append(time2)
#print(rssi2)
ind = np.arange(len(times1))  # the x locations for the groups
width = 0.35  # the width of the bars
time = times1 + times2

lopy1 = []
lopy2 = []
for val in range(0,len(rssi1)):
    lopy1.append((times1[val], numNets1[val]))
for val in range(0,len(rssi2)):
    lopy2.append((times2[val], numNets2[val]))

data = {'LoPy1': lopy1, 'Lopy4': lopy2}

time = []
label = []
value = []

for k, v in data.items():
    for tup in v:
        label.append(k)
        time.append(tup[0])
        value.append(tup[1])

df = pd.DataFrame({'time':time, 'label':label, 'value':value})

df = df.pivot(index='time', columns='label', values='value')

# Replace nans by forward filling existing values
df = df.fillna(method = 'ffill')

# You'll still have to handle the missing values in the beginning of the coloumns
df = df.fillna(method = 'bfill')

# A simple plot:
df.plot()
