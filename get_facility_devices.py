#!/usr/bin/env python3

import csv
import requests

url = 'https://api.decazavazduh.rs/api/devices/?limit=180'

csvheader = ['facility', 'device_id']

headers = {
  'Accept': 'application/json',
  'Content-type': 'application/json'
}

ourdata = []


response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()

for x in myjson['results']:
  if x['mode'] == 'PRODUCTION':
    ourdata.append([x['school_code'], x['device_id']])

with open('facility_devices.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(csvheader)
  writer.writerows(ourdata)

print('done')