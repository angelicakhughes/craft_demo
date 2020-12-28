#!/usr/bin/python3
import json
import requests
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

response = requests.get("https://www.travel-advisory.info/api")
filedata = response.json()
with open('data.json', 'w') as f:
	json.dump(filedata, f)
countrydata = filedata['data']

@app.route('/', methods=['GET','POST'])            
def index():                                           
	return countrydata 

@app.route('/diag', methods = ['GET'])
def api_hello():
    data = {
        'api_status': {
        'code' : 200,
	'status' : "good"
    }}
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'https://www.travel-advisory.z'

    return resp

@app.route('/convert', methods = ['GET'])
def convert():
	response = requests.get("https://www.travel-advisory.info/api")
	filedata = response.json()
	with open('data.json', 'w') as f:
                json.dump(filedata, f)
	countrydata = filedata['data']

	inputs = input("Enter a multiple country code values: ").split()

	for x in inputs:
		try:
                	return (countrydata[(x)]["name"])
		except KeyError:
	                return (x + ' country code does not exist. Please rerun the program without this country code')
		continue

@app.route('/health')
def health():
        return {'message': 'Healthy'} 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

