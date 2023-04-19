import unittest
import json
import os
import sqlite3
import requests


# def create_tables(db):
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"airports")
cur = conn.cursor()

#  cur.execute('DROP TABLE IF EXISTS airports')
cur.execute('CREATE TABLE IF NOT EXISTS airports (ID INTEGER, ICAO_code INTEGER, IATA_code INTEGER, name TEXT, location_ID INTEGER)')
cur.execute("CREATE TABLE IF NOT EXISTS airport_locations (ID INTEGER, country_ID INTEGER, weather_ID INTEGER, city TEXT, region TEXT, timezone TEXT, latitude INTEGER, longitute INTEGER, elevation INT)")
cur.execute("CREATE TABLE IF NOT EXISTS weather (ID INTEGER, country_ID INTEGER, air_quality_ID INTEGER, wind_speed INTEGER, wind_degrees INTEGER, temperature INTEGER, humidity INTEGER, sunrise INTEGER, sunset INTEGER, cloud_pct INTEGER, feels_like INTEGER, max_temp INTEGER, min_temp INTEGER)") 
 

cur.execute("SELECT * FROM airports")



# create_tables("airports")








