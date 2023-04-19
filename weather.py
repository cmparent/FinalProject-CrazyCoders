import unittest
import json
import os
import sqlite3
import requests


def get_data_weather(city):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)


def make_weather_table(cities, cur, conn):

    cur.execute("CREATE TABLE IF NOT EXISTS weather (ID INTEGER, country_ID INTEGER, air_quality_ID INTEGER, wind_speed INTEGER, wind_degrees INTEGER, temperature INTEGER, humidity INTEGER, sunrise INTEGER, sunset INTEGER, cloud_pct INTEGER, feels_like INTEGER, max_temp INTEGER, min_temp INTEGER)") 

    








