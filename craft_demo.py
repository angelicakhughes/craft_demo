#!/usr/bin/env python3
import logging
import requests
import json
import argparse
import sys
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

#import sqlite3
#conn = sqlite3.connect('example.db') 

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Started country code lookup')

## get request to Travel Advisory API
response = requests.get("https://www.travel-advisory.info/api")

## error if API endpoint not reachable
if response.status_code != 200:
	logging.error('An error occured trying to reach the API endpoint. Please check the Travel Advisory API')

## Save data from API to json file
filedata = response.json()
with open('data.json', 'w') as f:
    json.dump(filedata, f)


## Look up country by country code
countrydata = filedata['data']

inputs = input("Enter a multiple country code values: ").split()

print (inputs)
logging.info('Looking up countries')

try:
	for x in inputs:
		print (countrydata[(x)]["name"])
except KeyError:
    		print (x + ' country code does not exist. Please rerun the program without this country code')

@app.route("/")
def country_lookup():
  return "Here is the country lookup!"

@app.route('/diag', methods = ['GET'])
def api_hello():
    data = {
        'api_status': {
        'code' : 200,
        'status' : "ok"
    }}
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'https://www.travel-advisory.info/api'

    return resp




#PARSER = argparse.ArgumentParser(
#        description='Country Lookup Tool',
#        formatter_class=argparse.ArgumentDefaultsHelpFormatter
#    )
#PARSER.add_argument('-c', '--countryCode', type=str, help='Country Code') 
