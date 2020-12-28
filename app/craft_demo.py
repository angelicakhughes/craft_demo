#!/usr/bin/env python

import logging
import requests
import json
import traceback
import argparse
import sys
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Started country code lookup')

parser = argparse.ArgumentParser()
   
parser.add_argument('lookup')
parser.add_argument('--countrycode')

args = parser.parse_args()

#print(f'{args.lookup} is {args.countrycode} countrycode')

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

logging.info('Looking up countries')

for x in (args.countrycode).split(","):
        try:
                print (countrydata[(x)]["name"])
        except KeyError:
                print(bcolors.WARNING + (x) + " country code does not exist." + bcolors.ENDC)
                continue

logging.info('Country lookup complete.')
