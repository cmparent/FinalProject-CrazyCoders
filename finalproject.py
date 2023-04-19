import unittest
import json
import os
import sqlite3
import requests


# open database
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"airports")
cur = conn.cursor()

# make tables
cur.execute('CREATE TABLE IF NOT EXISTS airports (ID INTEGER, ICAO_code INTEGER, IATA_code INTEGER, name TEXT, location_ID INTEGER)')
cur.execute("CREATE TABLE IF NOT EXISTS airport_locations (ID INTEGER, country_ID INTEGER, weather_ID INTEGER, city TEXT, region TEXT, timezone TEXT, latitude INTEGER, longitute INTEGER, elevation INT)")
cur.execute("CREATE TABLE IF NOT EXISTS weather (ID INTEGER, country_ID INTEGER, air_quality_ID INTEGER, wind_speed INTEGER, wind_degrees INTEGER, temperature INTEGER, humidity INTEGER, sunrise INTEGER, sunset INTEGER, cloud_pct INTEGER, feels_like INTEGER, max_temp INTEGER, min_temp INTEGER)") 
cur.execute("CREATE TABLE IF NOT EXISTS country (ID INTEGER, gdp INTEGER, surface_area INTEGER, life_expectancy_male INTEGER, imports INTERGER, currency_name TEXT, urban_population_growth INTEGER, capital TEXT, co2_emissions INTEGER, tourists INTEGER, life_expectancy_female INTEGER, population INTEGER, urban_population INTEGER, name TEXT, pop_growth INTEGER, region INTEGER, pop_density INTEGER, refugees INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS air_quality (ID INTEGER, AQI INTEGER, CO INTEGER, PM10 INTEGER, SO2 INTEGER, PM25 INTEGER, O3 INTEGER, NO2 INTEGER)")

# weather API - get data

url = "https://api.api-ninjas.com/v1/weather?country={}".format(country)
# api_key = 
response = requests.get(url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
# print(response.text)

# country API

url1 = "'https://api.api-ninjas.com/v1/country?name=United States'
response1 = requests.get(url, headers = {'X-Api-Key': 'KXNSpXxVeBlWPPAuIjI3Cg==7Oe7vdmd05QCcjZ7'})

if response1.status_code == requests.codes.ok:
    print(response1.text)
else:
    print("Error:", response1.status_code, response.text)