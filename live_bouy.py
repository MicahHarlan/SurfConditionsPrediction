import urllib.request
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
np.set_printoptions(suppress=True)

"""
This file gets current data from NOAA.
The data is spectral wave data from the bouy near my surf spot.
"""

url = "https://www.ndbc.noaa.gov/data/realtime2/44099.spec"
response = urllib.request.urlopen(url)
data = np.loadtxt(response,delimiter=r'\s+',dtype="str")
new_data = []
#Cleaning The Data
new_data.append("#YY MM DD hh mm WVHT SwH SwP WWH WWP SwD WWD STEEPNESS APD MWD")
for l in data:
	l = l.replace("\n","")
	l = l.replace("   "," ")
	new_data.append(l.replace("  "," "))
waves = np.array(new_data)
columns = new_data[0].split(" ")
data = [line.split() for line in waves]
df = pd.DataFrame(data[1:], columns=data[0])

df['datetime'] = pd.to_datetime(df['#YY']+'-'+df['MM']+'-'+df['DD']+' '+df['hh']+':'+df['mm'])
df['date'] = pd.to_datetime(df['#YY']+'-'+df['MM']+'-'+df['DD'])
df['WVHT'] = df['WVHT'].astype(float)
today = pd.Timestamp.now().date()
mask = df["datetime"].dt.date == today
df_today = df.loc[mask]

time = pd.Timestamp.now()
closest_time_row = df_today.iloc[(df_today['datetime'] - time).abs().argsort()]
closest_time_row = closest_time_row.iloc[0]

"""
#PLOTTING WAVES 
figure, ax = plt.subplots(2)

ax[0].plot(df_today['datetime'], df_today['WVHT'])
ax[0].set_xlabel('Date and Time')
ax[0].set_ylabel('Wave Height (m)')
ax[0].set_title(f'Wave Height {today}')
"""

print(f"DATE: {today}")
print("IDEAL CONDITIONS") 
print("SWELL DIR: SE or E")
print("SWELL PERIOD: > 8 seconds")
print("WIND: SW, WSW, and or W")
print("-------------")
print(f"SWELL DIR: {closest_time_row['SwD']}")
print(f"SWEll PERIOD: {closest_time_row['SwP']} seconds")
print(f"WIND: {closest_time_row['WWD']}")
print(f"HEIGHT: {closest_time_row['WVHT']}")


#TIDE START

url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter'
params = {
    'station': '8638610', # station ID for Cape Henry Lighthouse
    'product': 'predictions',
    'begin_date': pd.Timestamp.now().floor('D').strftime('%Y%m%d'), # start date (today)
    'end_date': pd.Timestamp.now().strftime('%Y%m%d'), # end date (today)
    'datum': 'MLLW', # reference datum
    'units': 'english',
    'time_zone': 'lst_ldt',
    'format': 'json'
}
response = requests.get(url, params=params)


data = response.json()['predictions']
df = pd.DataFrame(data)
df['t'] = pd.to_datetime(df['t'])
df['v'] = pd.to_numeric(df['v'])
df['t'] = pd.to_datetime(df['t'], format='%Y-%m-%d %I:%M%p')



plt.xticks(pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min'),
		pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min').strftime('%I:%M%p')
		,rotation=45, ha='right')


# plot the tide data
plt.plot(df['t'], df['v'],linestyle='--',color='green',label='ForeCasted')
params['product'] = 'water_level'

response = requests.get(url, params=params)
data = response.json()['data']
df = pd.DataFrame(data)
df['t'] = pd.to_datetime(df['t'])
df['v'] = pd.to_numeric(df['v'])
df['v'] = pd.to_numeric(df['v'])
df['t'] = pd.to_datetime(df['t'], format='%Y-%m-%d %I:%M%p')



plt.plot(df['t'], df['v'],color='blue',label='Current')

#plt.xticks(pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min'),
#		pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min').strftime('%I:%M%p')
#		,rotation=45, ha='right')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Tide Height (m)')
plt.title(f'Tide For Virginia Beach {today}')






plt.show()
#TIDE END






















