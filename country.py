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

def createtable1(countries1, cur, conn):
    cur.execute("DROP TABLE IF EXISTS country")
    cur.execute("CREATE TABLE IF NOT EXISTS country (ID INTEGER, gdp INTEGER, surface_area INTEGER, life_expectancy_male INTEGER, imports INTERGER, currency_name TEXT, urban_population_growth INTEGER, capital TEXT, threatened_species TEXT, tourists INTEGER, life_expectancy_female INTEGER, population INTEGER, urban_population INTEGER, name TEXT, pop_growth INTEGER, region INTEGER, pop_density INTEGER, AQI_ID INTEGER, refugees INTEGER)")
    cur.execute("SELECT ID FROM country WHERE ID = (SELECT MAX(ID) FROM country)")

    count1 = 0

    first1 = cur.fetchone()

    if (first1 == None):
        first1 = 0
    else:
        first1 = first1[0] + 1

    for country in countries1[first1: first1+25]:
        countrydata = getdata(country)
    
        country_ID = first1 + count1

        try: 
            country_gdp = countrydata[0]['gdp']
        except:
            country_gdp = -1
        try: 
            country_SA = countrydata[0]['surface_area']
        except:
            country_SA = -1
        try: 
            country_LEM = countrydata[0]['life_expectancy_male']
        except:
            country_LEM = -1
        try: 
            country_imports = countrydata[0]['imports']
        except:
            country_imports = -1
        try: 
            country_currencyname = countrydata[0]['currency_name']
        except:
            country_currencyname = -1
        try: 
            country_UPG = countrydata[0]['urban_population_growth']
        except:
            country_UPG = -1
        try: 
            country_capital = countrydata[0]['capital']
        except:
            country_capital = -1
        try: 
            country_tourists = countrydata[0]['tourists']
        except:
            country_tourists = -1
        try: 
            country_LEF = countrydata[0]['life_expectancy_female']
        except:
            country_LEF = -1
        try: 
            country_TS = countrydata[0]['threatened_species']
        except:
            country_TS = -1
        try: 
            country_pop = countrydata[0]['population']
        except:
            country_pop = -1
        try: 
            country_UP = countrydata[0]['urban_population']
        except:
            country_UP = -1
        try: 
            country_name = countrydata[0]['name']
        except:
            country_name = -1
        try: 
            country_popgrowth = countrydata[0]['pop_growth']
        except:
            country_popgrowth = -1
        try: 
            country_region = countrydata[0]['region']
        except:
            country_region = -1
        try: 
            country_popdensity = countrydata[0]['pop_density']
        except:
            country_popdensity = -1
        try: 
            country_refugees = countrydata[0]['refugees']
        except:
            country_refugees = -1

        cur.execute("INSERT OR IGNORE INTO country (ID, gdp, surface_area, life_expectancy_male, imports, currency_name, urban_population_growth, capital, tourists, life_expectancy_female, threatened_species, population, urban_population, name, pop_growth, region, pop_density, AQI_ID, refugees) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(country_ID, country_gdp, country_SA, country_LEM, country_imports, country_currencyname, country_UPG, country_capital, country_tourists, country_LEF, country_TS, country_pop, country_UP, country_name, country_popgrowth, country_region, country_popdensity, country_ID, country_refugees))

        count1 += 1

    conn.commit()

def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    countries1 = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Honduras', 'Italy', 'Ireland', 'England', 'Canada','Poland', 'Sweden', 'Scotland', 'South Africa', 'Denmark', 'Iceland', 'UAE', 'Austria', 'Lebanon', 'Kenya', 'Peru', 'Nigeria', 'Ghana', 'Norway', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Lithuania', 'Andorra', 'Saudi Arabia', 'Iraq', 'Cameroon', 'Maldives', 'Cambodia', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Uzbekistan', 'Serbia', 'Moldova', 'Sri Lanka', 'Guinea', 'Latvia', 'Lithuania', 'Syria', 'Estonia', 'Bangladesh', 'Bulgaria', 'Myanmar', 'Qatar', 'Ireland', 'Tajikstan', 'Georgia', 'Tuvalu', 'Botswana', 'Guyana', 'Belarus', 'Mozambique', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Azerbaijan', 'Madagascar', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Singapore', 'Tunisia', 'Oman', 'Dominican Republic', 'Bolivia', 'Namibia', 'Paraguay', 'Comoros', 'Slovenia', 'Togo', 'Vanuatu', 'Seychelles', 'Zambia', 'Bosnia and Herzegovina', 'Croatia']

    createtable1(countries1, cur, conn)
    print("Added 25 rows to database!")

if __name__ == "__main__":
    main()