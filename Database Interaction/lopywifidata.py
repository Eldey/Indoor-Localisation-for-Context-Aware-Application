from flask import Flask, request
from flask_pymongo import PyMongo
import json
import requests
import om2m

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SMART_LoPy'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SMART_LoPy'

mongo = PyMongo(app)
	
@app.route("/monitorLopy1Wifi", methods=['POST'])
def lopy1_data():
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
		
		conn = mongo.db.WiFi_Data_1
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
def lopy2_data():
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
		
		conn = mongo.db.WiFi_Data_2
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
def lopy3_data():
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
		
		conn = mongo.db.WiFi_Data_3
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
def lopy4_data():
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
		
		conn = mongo.db.WiFi_Data_4
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
def lopy5_data():
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
		
		conn = mongo.db.WiFi_Data_5
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
def lopy6_data():
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
		
		conn = mongo.db.WiFi_Data_6
		data = {
			'Time' : time,
			'Networks' : names,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
if __name__ == '__main__':
	app.run('0.0.0.0', port=8083,debug=True)
	