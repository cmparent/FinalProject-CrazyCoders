import unittest
import sqlite3
import json
import os
import requests

def getdata(country):
    url1 = f'https://api.api-ninjas.com/v1/country?name={country}'
    response1 = requests.get(url1, headers={'X-Api-Key': 'KXNSpXxVeBlWPPAuIjI3Cg==7Oe7vdmd05QCcjZ7'})
    countrydata = json.loads(response1.text)

    return countrydata

def createtable1(countries, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS country (ID INTEGER, gdp INTEGER, surface_area INTEGER, life_expectancy_male INTEGER, imports INTERGER, currency_name TEXT, urban_population_growth INTEGER, capital TEXT, co2_emissions INTEGER, tourists INTEGER, life_expectancy_female INTEGER, population INTEGER, urban_population INTEGER, name TEXT, pop_growth INTEGER, region INTEGER, pop_density INTEGER, refugees INTEGER)")

    countries1 = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Thailand', 'Italy', 'Ireland', 'England', 'Canada','Mexico', 'Brazil', 'Australia', 'Netherlands', 'Denmark', 'Cuba', 'UAE', 'Austria', 'Czech Republic', 'Israel', 'Peru', 'Nigeria', 'Ghana', 'Ethiopia', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Kyrgyzstan', 'Guinea-Bissau', 'Colombia', 'Liberia', 'Barbados', 'Maldives', 'Romania', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Venezuela', 'Saint Lucia', 'Moldova', 'Sri Lanka', 'Guinea', 'Lesotho', 'Senegal', 'Syria', 'Tanzania', 'Bangladesh', 'Dijbouti', 'Monaco', 'Qatar', 'Ireland', 'Tajikstan', 'Sierra Leone', 'Tuvalu', 'Botswana', 'Guyana', 'Guatemala', 'Vietnam', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Uganda', 'Nepal', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Saint Vincent and the Grendadines', 'Democratic Republic of the Congo', 'Malaysia', 'Kuwait', 'Bolivia', 'Gabon', 'Malawi', 'North Korea', 'Slovenia', 'Togo', 'Svalbard and Jan Mayen', 'Angola', 'Zambia', 'Luxembourg', 'Croatia']
    print(len(countries))

    count1 = 0

    row1 = cur.fetchone()

    if (first1 == None):
        first1 = 0
    else:
        first1 = first1[0] + 1

    for country in countries1[first1: first1+25]:
        countrydata = getdata(country)
    
        country_id = first1 + count1
        country_gdp = countrydata[0]['gdp']
        country_SA = countrydata[0]['surface_area']
        country_LEM = countrydata[0]["life_expectancy_male"]
        country_imports = countrydata[0]["imports"]
        country_currencyname = countrydata[0]['currency_name']
        country_UPG = countrydata[0]['urban_population_growth']
        country_capital = countrydata[0]['capital']
        country_tourists = countrydata[0]['tourists']
        country_LEF = countrydata[0]['life_expectancy_female']
        country_TS = countrydata[0]['threatened_species']
        country_pop = countrydata[0]['population']
        country_UP = countrydata[0]['urban_population']
        country_name = countrydata[0]['name']
        country_popgrowth = countrydata[0]['pop_growth']
        country_region = countrydata[0]['region']
        country_popdensity = countrydata[0]['pop_density']
        country_AQIID = countrydata[0]['AQI_ID']
        country_refugees = countrydata[0]['refugees']

def main():

 countries1 = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Thailand', 'Italy', 'Ireland', 'England', 'Canada','Mexico', 'Brazil', 'Australia', 'Netherlands', 'Denmark', 'Cuba', 'UAE', 'Austria', 'Czech Republic', 'Israel', 'Peru', 'Nigeria', 'Ghana', 'Ethiopia', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Kyrgyzstan', 'Guinea-Bissau', 'Colombia', 'Liberia', 'Barbados', 'Maldives', 'Romania', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Venezuela', 'Saint Lucia', 'Moldova', 'Sri Lanka', 'Guinea', 'Lesotho', 'Senegal', 'Syria', 'Tanzania', 'Bangladesh', 'Dijbouti', 'Monaco', 'Qatar', 'Ireland', 'Tajikstan', 'Sierra Leone', 'Tuvalu', 'Botswana', 'Guyana', 'Guatemala', 'Vietnam', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Uganda', 'Nepal', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Saint Vincent and the Grendadines', 'Democratic Republic of the Congo', 'Malaysia', 'Kuwait', 'Bolivia', 'Gabon', 'Malawi', 'North Korea', 'Slovenia', 'Togo', 'Svalbard and Jan Mayen', 'Angola', 'Zambia', 'Luxembourg', 'Croatia']

# for country in countries:
#    getdata(country)

# main()