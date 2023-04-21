import unittest
import json
import os
import sqlite3
import requests


def get_data_weather(city):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    
    data = json.loads(response.text)
    
    return data

def create_weather_table(cities, cur, conn):
    
    # cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE IF NOT EXISTS weather (ID INTEGER PRIMARY KEY NOT NULL, city TEXT, wind_speed INTEGER, wind_degrees INTEGER, temperature INTEGER, humidity INTEGER, sunrise INTEGER, sunset INTEGER, cloud_pct INTEGER, feels_like INTEGER, max_temp INTEGER, min_temp INTEGER)")
    cur.execute("SELECT ID FROM weather WHERE ID = (SELECT MAX(ID) FROM weather)")

    count = 0

    first = cur.fetchone()

    if (first == None):
        first = 0
    else:
        first = first[0] + 1

    for city in cities[first: first + 25]:
        weather_city_data = get_data_weather(city)
        # print("City", city, weather_city_data)

        ID = first + count
        city_name = city

        try:
            cloud_pct = weather_city_data["cloud_pct"]
        except:
            cloud_pct = -1
        try:
            temp = weather_city_data["temp"]
        except:
            temp = -1
        try:
            feels_like = weather_city_data["feels_like"]
        except:
            feels_like = -1
        try:
            humidity = weather_city_data["humidity"]
        except:
            humidity = -1
        try:
            min_temp = weather_city_data["min_temp"]
        except:
            min_temp = -1
        try:
            max_temp = weather_city_data["max_temp"]
        except:
            max_temp = -1
        try:
            wind_speed = weather_city_data["wind_speed"]
        except:
            wind_speed = -1
        try:
            wind_deg = weather_city_data["wind_degrees"]
        except:
            wind_deg = -1
        try:
            sunrise = weather_city_data["sunrise"]
        except:
            sunrise = -1
        try:
            sunset = weather_city_data["sunset"]
        except:
            sunset = -1

        cur.execute("INSERT OR IGNORE INTO weather (ID, city, wind_speed, wind_degrees, temperature, humidity, sunrise, sunset, cloud_pct, feels_like, max_temp, min_temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, city_name, wind_speed, wind_deg, temp, humidity, sunrise, sunset, cloud_pct, feels_like, max_temp, min_temp))

        count += 1

    conn.commit()
        

def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Maracay", "Bexon", "Chisinau", "Colombo", "Conakry", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    # print(len(cities))

    create_weather_table(cities, cur, conn)
    print("Added 25 rows to the database!")

main()





