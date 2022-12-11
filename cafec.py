#!/usr/bin/env python3

import csv
import datetime
import requests

from_date = '2022-11-01'
until_date = '2022-11-30'

device_ids = [
  '3494540048AC',
  '3494540045EC',
  '0CDC7E3D8B7C',
  '0CDC7E3DB688',
  '0CDC7E3DE3F0',
  '349454002C8C',
  '0CDC7E3E1DD0',
  '0CDC7E3DB250',
  '0CDC7E3CAC70',
  '349454002C54',
  '3494540052A0',
  '3494540029D8',
  'A848FA94359C',
  'A848FA92A434',
  '349454004000',
  '0CDC7E3DA61C',
  '0CDC7E3EDAC0',
  'A848FA930B44',
  '0CDC7E3EFA3C',
  '0CDC7E3DED24',
  '349454004704',
  '349454004210',
  'A848FA93F400',
  '0CDC7E3DD45C',
  '0CDC7E3DD6EC',
  '0CDC7E3DC104',
  '0CDC7E3CE318',
  '0CDC7E3CB23C',
  '0CDC7E3DA0D4',
  '349454003168',
  'A848FA935914',
  '349454004EBC',
  '3494540041C4',
  '349454004448',
  '0CDC7E3EB50C',
  '349454004660',
  'A848FA93F3D4',
  '0CDC7E3DC33C',
  'A848FA93C99C',
  '349454002584',
  '349454004970',
  '0CDC7E3D9D40',
  'A848FA94558C',
  'A848FA939C00',
  '349454002FD4',
  'A848FA92EAFC',
  'A848FA93AD6C',
  '349454004054',
  '0CDC7E3D9E28',
  '0CDC7E3DA8D4',
  'A848FA942F88',
  '3494540034E4',
  '0CDC7E3DA880',
  '349454004634',
  'A848FA948A50',
  'A848FA942040',
  '3494540051F8',
  '349454004F48',
  '349454002CAC',
  'A848FA94569C',
  '3494540033F4',
  '3494540024C0',
  'A848FA9294CC',
  '0CDC7E3CD804',
  '0CDC7E3DA5A4',
  '3494540048EC',
  '0CDC7E3DA2F0',
  'A848FA9474B8',
  '0CDC7E3CF5E0',
  '0CDC7E3D9A54',
  '0CDC7E3DDC60',
  '3494540037AC',
  '0CDC7E3DE548',
  '0CDC7E3DCAD8',
  'A848FA93D9BC',
  '0CDC7E3D9BE0',
  'A848FA936150',
  '0CDC7E3CC028',
  '34945400557C',
  '3494540028BC',
  '349454003850',
  '349454004224',
  '0CDC7E3DA784',
  'A848FA942110',
  '0CDC7E3DE72C',
  '3494540021F8',
  'A848FA925D30',
  'A848FA929154',
  '349454003F00',
  '0CDC7E3ECFFC',
  '3494540033D4',
  '3494540040AC',
  '0CDC7E3EBC94',
  '0CDC7E3DA004',
  '0CDC7E3DDCFC',
  '0CDC7E3DA610',
  '0CDC7E3DD1C4',
  '0CDC7E3EFBEC',
  '0CDC7E3DD1CC',
  '349454002878',
  '0CDC7E3DCDB4',
  '0CDC7E3DD778',
  '0CDC7E3CF3BC',
  'A848FA946598',
  '349454004978',
  '3494540037EC',
  'A848FA9488DC',
  '0CDC7E3DCF04',
  '349454004A40',
  '349454005350',
  '349454002174',
  '349454002D90',
  '0CDC7E3DA5D0',
  'A848FA943ACC',
  '0CDC7E3DD474',
  '0CDC7E3CF558',
  'A848FA92C0F0',
  '349454002AD4',
  '0CDC7E3CC414',
  '0CDC7E3DC268',
  '349454002204',
  '349454004DC8',
  '0CDC7E3DE4C0',
  '0CDC7E3DB290',
  '0CDC7E3DE4DC',
  '349454004204',
  '0CDC7E3CF1E0',
  '0CDC7E3DCC6C',
  '0CDC7E3D9858',
  '0CDC7E3DCC4C',
  'A848FA935460',
  '349454004300',
  '349454000FB0',
  '0CDC7E3DD34C',
  '0CDC7E3E07A4'
]

url = 'https://api.decazavazduh.rs/api/devices/%s/data/aggregate/?interval=24h&from_date=%s&until_date=%s'

csvheader = ['device_id', 'date', 'has_results']

headers = {
  'Accept': 'application/json',
  'Content-type': 'application/json'
}

ourdata = []

def truncDate(iso_date):
  date_output = datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S")
  return date_output.date()


for device_id in device_ids:
  response = requests.request("GET", url % (device_id, from_date, until_date), headers=headers, data={})
  myjson = response.json()
  if(myjson['results'] == []):
    ourdata.append([device_id])

  for x in myjson['results']:
    ourdata.append([device_id, truncDate(x['time']), 1])


with open('2022-11.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(csvheader)
  writer.writerows(ourdata)

print('done')