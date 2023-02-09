#!/usr/bin/env python3

import csv
import calendar
import datetime
import requests

month = '2023-01'

def getFirstDate(month):
  dt = datetime.datetime.strptime(month, '%Y-%m')
  first_day = dt.replace(day=1)
  return first_day.strftime('%Y-%m-%d')

def getLastDate(month):
  dt = datetime.datetime.strptime(month, '%Y-%m')
  last_day_index = calendar.monthrange(dt.year, dt.month)[1]
  last_day = dt.replace(day=last_day_index)
  return last_day.strftime('%Y-%m-%d')

from_date = getFirstDate(month)
until_date = getLastDate(month)

devices_file = open("facility_devices.csv", "r")
devices = list(csv.DictReader(devices_file, delimiter=","))
devices_file.close()

url = 'https://api.decazavazduh.rs/api/devices/%s/data/aggregate/?interval=24h&from_date=%s&until_date=%s'

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
    ourdata.append([month, device['device_id'], device['facility']])

  for x in myjson['results']:
    ourdata.append([month, device['device_id'], device['facility'], truncDate(x['time']), x['pm1'], x['pm2_5'], x['pm10']])


with open('monthly_data.csv', 'a', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(ourdata)

print('done')
