#!/usr/bin/env python3

import csv
import datetime
import requests

from_date = '2022-11-01'
until_date = '2022-11-30'

devices_file = open("facility_devices.csv", "r")
devices = list(csv.DictReader(devices_file, delimiter=","))
devices_file.close()

url = 'https://api.decazavazduh.rs/api/devices/%s/data/aggregate/?interval=24h&from_date=%s&until_date=%s'

csvheader = ['device_id', 'facility', 'date', 'pm1', 'pm2_5', 'pm10']

headers = {
  'Accept': 'application/json',
  'Content-type': 'application/json'
}

ourdata = []

def truncDate(iso_date):
  date_output = datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S")
  return date_output.date()


for device in devices:
  response = requests.request("GET", url % (device['device_id'], from_date, until_date), headers=headers, data={})
  myjson = response.json()
  if(myjson['results'] == []):
    ourdata.append([device['device_id'], device['facility']])

  for x in myjson['results']:
    ourdata.append([device['device_id'], device['facility'], truncDate(x['time']), x['pm1'], x['pm2_5'], x['pm10']])
  
  print('.', end='')


with open('2022-11.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(csvheader)
  writer.writerows(ourdata)

print('done')