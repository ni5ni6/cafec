import datetime

date_string = '2022-11-30T00:00:00'

date_output = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

date = date_output.date();
print(date)