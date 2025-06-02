import json
import ssl
from urllib.request import urlopen

def main():
    firstUrl = "https://api.weather.gov/points/40.1934,-85.3864"
    firstcontext = ssl._create_unverified_context()
    response = urlopen(firstUrl, context=firstcontext)
    weatherData = json.loads(response.read())
    print(len(weatherData["properties"]))
    forecastUrl = weatherData["properties"]["forecast"]
    secondResponse = urlopen(forecastUrl, context=firstcontext)
    weatherDataTwo = json.loads(secondResponse.read())
    forecastPeriods = weatherDataTwo["properties"]["periods"]
    for period in forecastPeriods:
        print(f"Name: {period['name']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Forecast: {period['detailedForecast']}")
        print("")
    

main()