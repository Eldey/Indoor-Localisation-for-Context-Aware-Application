from flask import Flask, request
from flask_pymongo import PyMongo
import json
import requests
import om2m

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SMART_RPi'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SMART_RPi'

mongo = PyMongo(app)

	
@app.route("/monitor", methods=['POST'])
def save_data():
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
		
		conn = mongo.db.WiFi_Data
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
	app.run('0.0.0.0',port=8081,debug=True)
	