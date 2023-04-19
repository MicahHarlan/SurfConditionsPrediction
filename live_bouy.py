import urllib.request
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
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

#PLOTTING WAVES 
plt.plot(df_today['datetime'], df_today['WVHT'])
plt.xlabel('Date and Time')
plt.ylabel('Wave Height (m)')
plt.title(f'Wave Height {today}')
plt.show()
print(f"DATE: {today}")
print("IDEAL CONDITIONS") 
print("SWELL DIR: SE or E")
print("SWELL PERIOD: > 8 seconds")
print("WIND: SW, WSW, and or W")
print("-------------")
print(f"SWELL DIR: {closest_time_row['SwD']}")
print(f"SWEll PERIOD: {closest_time_row['SwP']}")
print(f"WIND:{closest_time_row['WWD']}")
print(f"HEIGHT: {closest_time_row['WVHT']}")
print("STILL NEED AIR TEMP, WATER TEMP, and TIDE")

#GETTING AIR TEMP
url = "https://www.ndbc.noaa.gov/data/realtime2/CHYV2.txt"
response = urllib.request.urlopen(url)
data = np.loadtxt(response,delimiter=r'\s+',dtype="str")
new_data = []

#Cleaning The Data

for l in data:
    l = l.replace("\n","")
    l = l.replace("   "," ")
    new_data.append(l.replace("  "," "))
waves = np.array(new_data)



