import unittest
import json
import os
import sqlite3
import requests


def get_data_air_quality(country):

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(country)
    response = requests.get(api_url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})

    response = requests.get(api_url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    data = json.loads(response.text)

    return data

def create_air_quality_table(cities, cur, conn):
    cur.execute("DROP TABLE IF EXISTS air_quality")
    cur.execute("CREATE TABLE IF NOT EXISTS air_quality (ID INTEGER PRIMARY KEY, city TEXT, AQI INTEGER, CO INTEGER, PM10 INTEGER, SO2 INTEGER, PM25 INTEGER, O3 INTEGER, NO2 INTEGER)")
    cur.execute("SELECT ID FROM air_quality WHERE ID = (SELECT MAX(ID) FROM air_quality)")

    count = 0

    first = cur.fetchone()
    if first == None:
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
        try: 
            carbon_monoxide = air_data["CO"]["concentration"]
        except:
            carbon_monoxide = -1

        cur.execute("INSERT OR IGNORE INTO air_quality (ID, city, AQI, CO) VALUES (?, ?, ?, ?)",(ID, city_name, AQI, carbon_monoxide))

        count += 1

    conn.commit()


def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Maracay", "Bexon", "Chisinau", "Colombo", "Conakry", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    # print(len(cities))

    create_air_quality_table(cities, cur, conn)


main()