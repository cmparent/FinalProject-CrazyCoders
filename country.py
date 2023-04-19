import unittest
import sqlite3
import json
import os
import requests

def getdata(country):
    url1 = f'https://api.api-ninjas.com/v1/country?name={country}'
    response1 = requests.get(url1, headers={'X-Api-Key': 'KXNSpXxVeBlWPPAuIjI3Cg==7Oe7vdmd05QCcjZ7'})
    if response1.status_code == requests.codes.ok:
        print(response1.text)
    else:
        print("Error:", response1.status_code, response1.text)


def createtable1(countries, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS country (ID INTEGER, gdp INTEGER, surface_area INTEGER, life_expectancy_male INTEGER, imports INTERGER, currency_name TEXT, urban_population_growth INTEGER, capital TEXT, co2_emissions INTEGER, tourists INTEGER, life_expectancy_female INTEGER, population INTEGER, urban_population INTEGER, name TEXT, pop_growth INTEGER, region INTEGER, pop_density INTEGER, refugees INTEGER)")