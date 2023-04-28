import requests
import json

# Define the API endpoint and parameters
endpoint = 'https://services.surfline.com/kbyg/spots/forecasts'
params = {
    'spotId': '584204214e65fad6a7709ce7',  # Virginia Beach spot ID
    'days': '5',  # Number of forecast days
    'intervalHours': '1',  # Forecast interval (in hours)
    'maxHeights': True,  # Include maximum surf height
    'showWind': True,  # Include wind data
    'units': 'e',  # Units (e=English, m=Metric)
}

# Make the API request and parse the response
response = requests.get(endpoint, params=params)
data = json.loads(response.text)

# Extract the relevant forecast variables
for forecast in data['data']['forecasts']:
    date = forecast['date']['pretty']
   

