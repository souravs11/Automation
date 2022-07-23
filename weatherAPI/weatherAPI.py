###
# Target Release:       1.0
# Code Status:          Complete
# Code Developer:       Sourav
# Script Name:          weatherAPI.py
# How to run:           python3 weatherAPI.py YOUR_API_KEY CITY_NAME
###

import requests     # 'requests' module allows you to send HTTP requests.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
import sys          # 'sys' module allows you to access the arguments.

# MANUAL OVERRIDE: You can hard-code your API key below, but it's not recommended from security perspective.
# API_KEY = "YOUR 32 CHARACTER LONG API KEY GOES HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"    # This is the Base URL
API_KEY = sys.argv[1]   # Reading API Key from the arguments passed
CITY = sys.argv[2]      # Reading the city name from the arguments passed

# MANUAL OVERRIDE: If you do not want to pass the API key during script trigger-call. Follow this:
# test_api = input("Enter API Key:")
# print(test_api)

REQUEST_URL = f"{BASE_URL}?appid={API_KEY}&q={CITY}"     # Formation of API endpoint URL
# print(REQUEST_URL)

if len(sys.argv) == 3:
    print(f'This is your API Key: \t\t\t',API_KEY)
    print(f'This is the city you are interested in: {CITY.upper()}.')
    weather_response = requests.get(REQUEST_URL)        # Sending a GET Request
    if weather_response.status_code == 200:             # Proceeding only if we are able to retrieve weather data successfully
        print(f'SUCCESSFUL!')
        response_data = weather_response.json()
        current_weather = response_data['weather'][0]['description']            # Reading weather description from the JSON response.
        current_temperature = round(response_data['main']['temp'] - 273.15,2)   # Reading temperature from the JSON response.
        print(f'Current weather is - {current_weather} ... and the temperature is {current_temperature}°C.')
    else:                                               # When the weather data is unavailable.
        print('UNSUCCESSFUL! An error occured with status code: ', weather_response.status_code)
else:                                                   # This script only accepts API key and City name as arguments.
    print(f'Arghhh!! Not the number of arguments I expected!')