from flask import Flask, request
from flask_pymongo import PyMongo
import json
import requests
import om2m

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SMART_LoPy'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SMART_LoPy'

mongo = PyMongo(app)
	
@app.route("/monitorLopy1BT", methods=['POST'])
def lopy1_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_1
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
@app.route("/monitorLopy2BT", methods=['POST'])
def lopy2_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_2
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy3BT", methods=['POST'])
def lopy3_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_3
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy4BT", methods=['POST'])
def lopy4_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_4
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy5BT", methods=['POST'])
def lopy5_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_5
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}

@app.route("/monitorLopy6BT", methods=['POST'])
def lopy6_data():
	payload = None
	
	if "m2m:nev" in request.json["m2m:sgn"]:
		payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

		time = request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ct"]
		macs = payload['MAC Addresses']
		strengths = payload['Signal Strengths']
				
		conn = mongo.db.BT_Data_6
		data = {
			'Time' : time,
			'MAC Addresses' : macs,
			'Signal Strengths' : strengths
		}
		conn.insert(data)
		
		return('Saved')
		
	return "", 200, {'X-M2M-RSC': '2000'}
	
if __name__ == '__main__':
	app.run('0.0.0.0', port=8084,debug=True)
	