import unittest
import json
import os
import sqlite3
import requests


def get_data_air_quality(city):

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers = {'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    data = json.loads(response.text)

    # print(data)

def create_air_quality_table(cities, cur, conn):
    cur.execute("DROP TABLE IF EXISTS air_quality")
    cur.execute("CREATE TABLE IF NOT EXISTS air_quality (ID INTEGER PRIMARY KEY, AQI INTEGER, CO INTEGER, PM10 INTEGER, SO2 INTEGER, PM25 INTEGER, O3 INTEGER, NO2 INTEGER)")


def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Paris', 'Barcelona', 'Lisbon', 'Berlin', 'Brussel', 'Shanghai', 'Tokyo', 'Seoul', 'Bangkok', 'Rome', 'Dublin', 'London', 'Toronto', 'Mexico City', 'Rio de Janeiro', 'Sydney', 'Amsterdam', 'Copenhagen', 'Havana', 'Dubai', 'Vienna', 'Wellington', 'Prague', 'Jerusalem', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Chisinau", "Colombo", "Conarky", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    # print(len(cities))

main()