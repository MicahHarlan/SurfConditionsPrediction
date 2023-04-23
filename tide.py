import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True)
url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter'
params = {
    'station': '8638610', # station ID for Cape Henry Lighthouse
    'product': 'water_level',
    'begin_date': pd.Timestamp.now().floor('D').strftime('%Y%m%d'), # start date (today)
    'end_date': pd.Timestamp.now().strftime('%Y%m%d'), # end date (today)
    'datum': 'MLLW', # reference datum
    'units': 'english',
    'time_zone': 'lst_ldt',
    'format': 'json'
}

response = requests.get(url, params=params)
data = response.json()['data']
df = pd.DataFrame(data)
df['t'] = pd.to_datetime(df['t'])
#df = df.set_index('t')
df['v'] = pd.to_numeric(df['v'])

df['t'] = pd.to_datetime(df['t'], format='%Y-%m-%d %I:%M%p')



# plot the tide data
plt.plot(df['t'], df['v'])

plt.xticks(pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min'), 
           pd.date_range(start=df['t'].iloc[0], end=df['t'].iloc[-1], freq='60min').strftime('%I:%M%p'), 
           rotation=45, ha='right')

plt.xlabel('Time')
plt.ylabel('Tide Height (m)')
plt.title('Tide Graph')
plt.show()
