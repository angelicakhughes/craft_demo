#!/bin/bash
  
#export from api to file
curl https://www.travel-advisory.info/api -o "data.json"

#convert to comma seperate and quotes
codes=`echo $1 | sed -e 's/^/"/' -e 's/\$/"/' -e 's/,/",\"/g'`

jq ".data | .[$codes] | .name" data.json
