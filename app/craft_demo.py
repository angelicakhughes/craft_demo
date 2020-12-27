#!/usr/bin/env python3

import logging
import requests
import json
import argparse
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Started country code lookup')

# get request to Travel Advisory api
response = requests.get("https://www.travel-advisory.info/api")

# error if api endpoint not reachable
if response.status_code != 200:
	logging.error('An error occured trying to reach the API endpoint. Please check the Travel Advisory API')

# save data from api to json file
filedata = response.json()
with open('data.json', 'w') as f:
    json.dump(filedata, f)

# Look up country by country code
countrydata = filedata['data']

inputs = input(bcolors.OKBLUE + "Enter a multiple country code values: " + bcolors.ENDC).split()

logging.info('Looking up countries')

for x in inputs:
	try:
		print (countrydata[(x)]["name"])
	except KeyError:
		print(bcolors.WARNING + (x) + " country code does not exist." + bcolors.ENDC)
		continue

#PARSER = argparse.ArgumentParser(
#        description='Country Lookup Tool',
#        formatter_class=argparse.ArgumentDefaultsHelpFormatter
#    )
#PARSER.add_argument('-c', '--countryCode=', type=inputs, help='Country Code')
