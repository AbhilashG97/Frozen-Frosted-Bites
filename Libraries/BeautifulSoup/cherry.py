# A simple python script that scraps data from 
# a weather site. 

# Link to the site - https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XI-bXigza00

from bs4 import BeautifulSoup
import pandas as pd
import requests

webpage = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XI-bXigza00')

print(webpage.status_code)

weather = BeautifulSoup(webpage.content, 'html.parser')

# Get the forecast list
seven_day_weather = weather.find(id='seven-day-forecast-list')

print(seven_day_weather.prettify())

# Get the forecast
forecast_items = seven_day_weather.find_all(class_='tombstone-container')

print("\n\n\n")

# examining a part of the data stored in a list
print(forecast_items[0].prettify())

print([tag.get_text() for tag in forecast_items])

forecast = forecast_items[0]

print(forecast.prettify())

print(forecast.find(class_="period-name").get_text())
print(forecast.find(class_="short-desc").get_text())
print(forecast.find(class_="temp temp-high").get_text())
print(forecast.find("img", class_="forecast-icon")['title'])

# Getting necessary tags
period_tags = seven_day_weather.select(".tombstone-container .period-name")
short_descriptions = seven_day_weather.select(".tombstone-container .short-desc")
highest_temperature = seven_day_weather.select(".tombstone-container .temp")
detail_desc = seven_day_weather.select(".tombstone-container .forecast-icon")

# Extracting the data
days = [day.get_text() for day in period_tags]
short_desc = [desc.get_text() for desc in short_descriptions]
temperatures = [temp.get_text() for temp in highest_temperature]
details = [desc['title'] for desc in detail_desc]

print(days)
print(short_desc)
print(temperatures)
print(details)

data = pd.DataFrame({
    'days' : days,
    'short description' : short_desc,
    'temperatures' : temperatures,
    'more information' : details
})

print(data)
data.to_csv('weather-data.csv', sep=',')