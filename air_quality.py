import unittest
import json
import os
import sqlite3
import requests


def get_data_air_quality(country):

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(country)
    response = requests.get(api_url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    data = json.loads(response.text)

    return data

def create_air_quality_table(cities, cur, conn):
    # cur.execute("DROP TABLE IF EXISTS air_quality")
    cur.execute("CREATE TABLE IF NOT EXISTS air_quality (ID INTEGER PRIMARY KEY, city TEXT, AQI INTEGER, CO INTEGER)")
    cur.execute("SELECT ID FROM air_quality WHERE ID = (SELECT MAX(ID) FROM air_quality)")

    count = 0

    first = cur.fetchone()
    if (first == None):
        first = 0
    else:
        first = first[0] + 1

    for city in cities[first:first + 25]:
        air_data = get_data_air_quality(city)
        # print(air_data)

        ID = first + count
        city_name = city

        try:
            AQI = air_data["overall_aqi"]
        except:
            AQI = -1
        # print(AQI)
        try: 
            carbon_monoxide = air_data["CO"]["concentration"]
        except:
            carbon_monoxide = -1
        # print(carbon_monoxide)


        cur.execute("INSERT OR IGNORE INTO air_quality (ID, city, AQI, CO) VALUES (?, ?, ?, ?)",(ID, city_name, AQI, carbon_monoxide))

        count += 1

    conn.commit()


def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Lagos", "Tema", "Oslo", "Oran", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Sikasso", "Seria", "Bangui", "Banjul", "Vilnius", "Encamp", "Riyadh", "Baghdad", "Male", "Douala", "Brussels", "Phnom Penh", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Tashkent", "Belgrade", "Chisinau", "Colombo", "Conakry", "Riga", "Vilnius", "Damascus", "Tallinn", "Dhaka", "Sofia", "Yangon", "Doha", "Dublin", "Dushanbe", "Tbilisi", "Funafuti", "Gaborone", "Georgetown", "Minsk", "Maputo", "Harare", "Honiara", "Islamabad", "Surabaya", "Kabul", "Baku", "Antananarivo", "Khartoum", "Kiev", "Kigali", "Kingston", "Singapore", "Tunis", "Muscat", "Santo Domingo", "La Paz", "Skopje", "Tripoli", "Moroni", "Lome", "Mayen", "Port Vila", "Victoria", "Lusaka", "Sarajevo", "Zagreb"]
    # print(len(cities))

    create_air_quality_table(cities, cur, conn)
    "Added 25 rows to database!"

main()