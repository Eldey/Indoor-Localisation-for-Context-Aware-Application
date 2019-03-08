from flask import Flask, request
from flask_pymongo import PyMongo
import json
import requests
import om2m

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SMART'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SMART'

mongo = PyMongo(app)

@app.route("/monitorRpi1Wifi", methods=['POST'])
def rpi1_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])
		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		

		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Rpi1
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
@app.route("/monitorLopy1Wifi", methods=['POST'])
def lopy1_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy1
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy2Wifi", methods=['POST'])
def lopy2_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy2
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
@app.route("/monitorLopy3Wifi", methods=['POST'])
def lopy3_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy3
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy4Wifi", methods=['POST'])
def lopy4_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy4
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy5Wifi", methods=['POST'])
def lopy5_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy5
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy6Wifi", methods=['POST'])
def lopy6_wifi_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		names = payload['Networks']
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
		
		#print(names)
		#print(macs)
		#print(strengths)
		
		conn = mongo.db.WiFi_Data_Lopy6
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy1BT", methods=['POST'])
def lopy1_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy1
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
@app.route("/monitorLopy2BT", methods=['POST'])
def lopy2_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy2
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy3BT", methods=['POST'])
def lopy3_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy3
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy4BT", methods=['POST'])
def lopy4_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy4
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy5BT", methods=['POST'])
def lopy5_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy5
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy6BT", methods=['POST'])
def lopy6_bt_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_Lopy6
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
if __name__ == '__main__':
	app.run('0.0.0.0', port=8081,debug=True)
	