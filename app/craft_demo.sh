#!/bin/bash
#Usage: ./craft_demo.sh AL,BE,GE,LI,FI
  
#export from api to json file
curl https://www.travel-advisory.info/api -o "data.json"

#convert to comma seperate and quotes
codes=`echo $1 | sed -e 's/^/"/' -e 's/\$/"/' -e 's/,/",\"/g'`

jq ".data | .[$codes] | .name" data.json
