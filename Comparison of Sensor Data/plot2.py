from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt

client = MongoClient('localhost',27017)
lopy1Wifi = client.SMART.WiFi_Data_Lopy1
lopy2Wifi = client.SMART.WiFi_Data_Lopy2

numNets1 = []
times1 = []
numNets2 = []
times2 = []
rssi1 = []
rssi2 = []

for item in lopy1Wifi.find({ '$and' : [{'Time': {'$gte': '20190221T162520'}}, {'Time': {'$lt': '20190221T164030'}}]}):
    numNets1.append(len(item['Networks']))
    pos = item['Networks'].index('TelstraD293DF')
    rssi1.append(item['Signal Strengths'][pos])
    time1 = item['Time'][9:]
    time1 = ':'.join(time1[i:i+2] for i in range(0, len(time1), 2))
    times1.append(time1)
#print(rssi1)
for item in lopy2Wifi.find({ '$and' : [{'Time': {'$gte': '20190221T162520'}}, {'Time': {'$lt': '20190221T164030'}}]}):
    numNets2.append(len(item['Networks']))
    pos = item['Networks'].index('TelstraD293DF')
    rssi2.append(item['Signal Strengths'][pos])
    time2 = item['Time'][9:]
    time2 = ':'.join(time2[i:i+2] for i in range(0, len(time2), 2))
    times2.append(time2)
#print(rssi2)
ind = np.arange(len(times1))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(ind - width/2, rssi1, width, color='SkyBlue', label='LoPy1')
#rects2 = ax.bar(ind + width/2, rssi2, width, color='IndianRed', label='LoPy2')
line1 = ax.plot(times1, rssi1, color='SkyBlue', label='LoPy1')
line1 = ax.plot(times1, rssi2, color='IndianRed', label='LoPy2')
ax.set_ylabel('Signal Strength')
ax.set_title('Strength of TelstraD293DF between 16:25 and 16:40')
ax.set_xticks(ind)
ax.set_xticklabels(times1, fontsize = 'x-small', wrap = True)
ax.legend()


plt.show()
#print()