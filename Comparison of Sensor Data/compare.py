from pymongo import MongoClient
import pprint

def duplicates(lst, item):
	return [i for i, x in enumerate(lst) if x == item]

def eduroam():
	print()

client1 = MongoClient('mongodb+srv://cdf999:smart123@cluster0-nkwdw.mongodb.net/SMART_RPi?retryWrites=true')
rpi = client1.SMART_RPi
rpiWifi = rpi.WiFi_Data

client2 = MongoClient('mongodb+srv://cdf999:smart123@cluster0-nkwdw.mongodb.net/SMART_LoPy?retryWrites=true')
lopy = client2.SMART_LoPy
lopyWifi = lopy.WiFi_Data


rdata = rpiWifi.find_one(skip = 2)
ldata = lopyWifi.find_one(skip = 2)

common = 0
coms = []

for item in rdata['MAC Addresses']:
	if item in ldata['MAC Addresses']:
		common += 1
		r = rdata['MAC Addresses'].index(item)
		l = ldata['MAC Addresses'].index(item)
		coms.append((rdata['Networks'][r], item, rdata['Signal Strengths'][r], ldata['Signal Strengths'][l]))
	
	
print('RPi sees ', len(rdata['MAC Addresses']), ' networks')
print('LoPy sees ', len(ldata['MAC Addresses']), ' networks')
print(common, ' are common')

for x in range(0,len(coms)):
	print(coms[x])


#lopyWifi.find_one({'Time': {'$gt': '20190221T162500'}})