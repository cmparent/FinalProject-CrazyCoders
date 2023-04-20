import unittest
import json
import os
import sqlite3
import requests


def get_data_air_quality(city):

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    data = json.loads(response.text)

    return data

def create_air_quality_table(cities, cur, conn):
    cur.execute("DROP TABLE IF EXISTS air_quality")
    cur.execute("CREATE TABLE IF NOT EXISTS air_quality (ID INTEGER PRIMARY KEY, city TEXT, AQI INTEGER, CO INTEGER, PM10 INTEGER, SO2 INTEGER, PM25 INTEGER, O3 INTEGER, NO2 INTEGER)")

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
        AQI = air_data["overall_aqi"]
        CO = air_data["CO"]["concentration"]
        PM10 = air_data["PM10"]["concentration"]
        SO2 = air_data["SO2"]["concentration"]
        PM25 = air_data["PM2.5"]["concentration"]
        O3 = air_data["O3"]["concentration"]
        NO2 = air_data["NO2"]["concentration"]

        cur.execute("INSERT OR IGNORE INTO air_quality (ID, city, AQI, CO, PM10, SO2, PM25, O3, NO2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(ID, city_name, AQI, CO, PM10, SO2, PM25, O3, NO2))

        count += 1

    conn.commit()





def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Paris', 'Barcelona', 'Lisbon', 'Berlin', 'Brussel', 'Shanghai', 'Tokyo', 'Seoul', 'Bangkok', 'Rome', 'Dublin', 'London', 'Toronto', 'Mexico City', 'Rio de Janeiro', 'Sydney', 'Amsterdam', 'Copenhagen', 'Havana', 'Dubai', 'Vienna', 'Wellington', 'Prague', 'Jerusalem', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Chisinau", "Colombo", "Conarky", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    # print(len(cities))

    create_air_quality_table(cities, cur, conn)




main()