import pandas as pd
import json
import requests
from datetime import date,timedelta


start_time = date.today()-timedelta(days=1)
start_time=str(start_time) + 'T00:00:00Z'


wind_df=pd.read_json('wind_' + str(start_time)+'.txt')
consumption_df=pd.read_json('consumption_' + str(start_time)+'.txt')

wind_sum=wind_df['value'].sum()
consumption_sum=consumption_df['value'].sum()

#print(consumption_sum)
daily_delta=(wind_sum/consumption_sum)

result ={"date": str(start_time), "percentage_wind": wind_sum/consumption_sum}

#result = {"date": yesterday, "percentage_wind": df_wind['value'].sum() / df_consumption['value'].sum()}

with open('result.json', 'a') as f:
    f.write(str(result) + '\n')

