import om2m
from network import WLAN, Bluetooth
import ubinascii
import json
import time

def getWifiConnectivity(networks):
    names = []
    macs = []
    strengths = []

    for row in range(0,len(networks)):
        names.append(networks[row].ssid)

        mac = ubinascii.hexlify(networks[row].bssid)
        macs.append( (mac.decode('ASCII')).upper() )
        
        strengths.append(networks[row].rssi)

    return {'names':names, 'macs':macs, 'strengths':strengths}

def getBTConnectivity(networks):
    macs = []
    strengths = []
    
    for network in range(0,len(networks)):
        m = ubinascii.hexlify(networks[network].mac)
        macs.append( (m.decode('ASCII')).upper() )
        strengths.append(networks[network].rssi)

    unique = list(set(macs))
    avgMacs =[]
    for item in range(0,len(unique)):
        indices = [i for i, v in enumerate(macs) if v == unique[item]]
        total = 0
        for index in indices:
            total += strengths[index]
        
        avg = round(total/len(indices))
        avgMacs.append(avg)

    return {'macs':unique, 'strengths':avgMacs}

def main():
    first = True
    while True:
        if first == True:
            om2m.createApplication('http://smart-iot.lan.uow.edu.au:8181/~/in-cse', 'admin:admin', 'LOPY5')
            om2m.createContainer('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5', 'admin:admin', 'WiFi_Connectivity')
            om2m.subscribeResource('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5/WiFi_Connectivity', 'admin:admin', 'lopy5_wifi_sub', 'http://smart-iot.lan.uow.edu.au:8081/monitorLopy5Wifi')
            

        wlan = WLAN()
        wlan.init(mode=WLAN.STA)
        wfResults = wlan.scan()

        wifiCon = getWifiConnectivity(wfResults)
        print('WiFi Connectivity:')
        print(wifiCon)
        print(len(wifiCon['names']))
        wifiData = {
            'Networks': wifiCon['names'],
            'MAC Addresses': wifiCon['macs'],
            'Signal Strengths': wifiCon['strengths']
        }
        om2m.createContentInstance('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5/WiFi_Connectivity', 'admin:admin', json.dumps(wifiData) )

        if first == True:
            om2m.createContainer('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5', 'admin:admin', 'BT_Connectivity')
            om2m.subscribeResource('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5/BT_Connectivity', 'admin:admin', 'lopy5_bt_sub', 'http://smart-iot.lan.uow.edu.au:8081/monitorLopy5BT')
            first = False

        bluetooth = Bluetooth()
        bluetooth.start_scan(3)
        while bluetooth.isscanning():
            time.sleep(1)
        btResults = bluetooth.get_advertisements()
        btCon = getBTConnectivity(btResults)
        print('BT Connectivity:')
        print(btCon)
        btData = {
            'MAC Addresses': btCon['macs'],
            'Signal Strengths': btCon['strengths']
        }
        om2m.createContentInstance('http://smart-iot.lan.uow.edu.au:8181/~/in-cse/in-name/LOPY5/BT_Connectivity', 'admin:admin', json.dumps(btData) )
        time.sleep(30)


if __name__ == '__main__':
    try:
        main()
    except:
        machine.reset()