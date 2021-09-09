import requests
import json
from datetime import date,timedelta

PERSONAL_CODE = {"x-api-key": "xyG378rZAv8l9OBDbSw7i9IUwXc8zj2z1dNixGZA"}
start_time = date.today()-timedelta(days=1)
end_time=str(start_time) + 'T23:59:00Z'
start_time=str(start_time) + 'T00:00:00Z'
time = {'start_time': start_time, 'end_time': end_time }

wind_id = 75
cons_id = 124


r_wind = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(wind_id), headers=PERSONAL_CODE, params = time)
r_consumption = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(cons_id), headers=PERSONAL_CODE, params=time)
print(r_wind.text)
print(r_consumption.text)

wind_file_name = 'wind_' + str(start_time)+'.txt'
consumption_file_name = 'consumption_' + str(start_time)+'.txt'
print(wind_file_name)

f = open(wind_file_name, 'w')
f.write (json.dumps(r_wind.json()))
f.close()

g = open(consumption_file_name, 'w')
g.write (json.dumps(r_consumption.json()))
g.close()









