#!/usr/bin/env python3

import datetime
import calendar

month = '2022-11'


dt = datetime.datetime.strptime(month, '%Y-%m')
print(dt)

first_day = dt.replace(day=1)
print("first date: ", first_day.strftime('%Y-%m-%d'))

last_day_index = calendar.monthrange(dt.year, dt.month)[1]
last_day = dt.replace(day=last_day_index)
print("last day: ", last_day.strftime('%Y-%m-%d'))