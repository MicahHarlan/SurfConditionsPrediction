import requests
import json
import pandas as pd

# Define the API endpoint
endpoint = 'https://api.tidesandcurrents.noaa.gov/api/datagetter'

# Set the request parameters
params = {
    'product': 'water_level',
    'application': 'PRODUCT_SPECIFIC_TOOL',
    'datum': 'STND',
    'units': 'english',
    'time_zone': 'lst_ldt',
    'format': 'json',
    'station': '8638863',  # Virginia Beach station ID
    'date': 'latest'
}

# Make the request and extract the water level
response = requests.get(endpoint, params=params)
data = json.loads(response.content)
water_level = data['data'][0]['v']
print(f"Current water level: {water_level} feet")

