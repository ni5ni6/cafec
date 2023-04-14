#!/usr/bin/env python3

import csv
import requests

municipality_code = 'uzice'
from_date = '2022-04-01'
until_date = '2023-03-31'

municipality_url = 'https://api.decazavazduh.rs/api/municipalities/%s/'
facility_report_url = 'https://api.decazavazduh.rs/api/facilities/%s/data/aggregate/?interval=1h&from_date=%s&until_date=%s&limit=1000'

def get_data(url):
  page = session.get(url).json()
  yield page

  while(page['next']):
    page = session.get(page['next']).json()
    yield page

school_codes = []

session = requests.Session()

response = session.get(municipality_url % municipality_code).json()
for school in response['schools']:
  school_codes.append(school['code'])

ourdata = []

for school_code in school_codes:
  url = facility_report_url % (school_code, from_date, until_date)
  for data in get_data(url):
    for x in data['results']:
      ourdata.append([school_code, x['time'], x['pm1'], x['pm2_5'], x['pm10']])

with open('custom_report.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['school_code', 'time', 'pm1', 'pm2_5', 'pm10'])
  writer.writerows(ourdata)

print('done')
