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

for item in lopy1Wifi.find({ '$and' : [{'Time': {'$gte': '20190221T162520'}}, {'Time': {'$lt': '20190221T164030'}}]}):
    numNets1.append(len(item['Networks']))
    time1 = item['Time'][9:]
    time1 = ':'.join(time1[i:i+2] for i in range(0, len(time1), 2))
    times1.append(time1)

for item in lopy2Wifi.find({ '$and' : [{'Time': {'$gte': '20190221T162520'}}, {'Time': {'$lt': '20190221T164030'}}]}):
    numNets2.append(len(item['Networks']))
    time2 = item['Time'][9:]
    time2 = ':'.join(time2[i:i+2] for i in range(0, len(time2), 2))
    times2.append(time2)

ind = np.arange(len(times1))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, numNets1, width, color='SkyBlue', label='LoPy1')
rects2 = ax.bar(ind + width/2, numNets2, width, color='IndianRed', label='LoPy2')
ax.set_ylabel('Number of Networks')
ax.set_title('Networks Seen between 16:25 and 16:40')
ax.set_xticks(ind)
ax.set_xticklabels(times1, fontsize = 'x-small', wrap = True)
ax.legend()


plt.show()
#print()