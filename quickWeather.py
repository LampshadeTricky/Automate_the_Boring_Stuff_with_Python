#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from commandline arguments.
if len(sys.argv) <2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f'http://api.openweathermap.org/data/2.5/forecast/weather?q={location}&cnt=3&appid=45a6012691e1ebdf648705429a037353'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print(f'Current weather in {location}')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])