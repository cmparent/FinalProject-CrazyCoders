import unittest
import sqlite3
import json
import os
import requests

def get_data(city):

    airport_url = 'https://api.api-ninjas.com/v1/airports?name={}'.format(city)
    airport_response = requests.get(airport_url, headers = {'X-Api-Key': 'UlC4xXn/1yAqzYBvCS/Wkg==EJ2pSOpCn3TEU3iQ'})
    
    if airport_response.status_code == requests.codes.ok:
        print(airport_response.text)
    else:
        print("Error:", airport_response.status_code, airport_response.text)


def create_table(cities, cur, conn):

    cur.execute('CREATE TABLE IF NOT EXISTS airports (ID INTEGER, ICAO_code INTEGER, IATA_code INTEGER, name TEXT, location_ID INTEGER)')
    
    cur.execute("CREATE TABLE IF NOT EXISTS airport_locations (ID INTEGER, country_ID INTEGER, weather_ID INTEGER, city TEXT, region TEXT, timezone TEXT, latitude INTEGER, longitute INTEGER, elevation INT)")

