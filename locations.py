import unittest
import sqlite3
import json
import os
import requests


def get_location_data(city):

    airport_url = 'https://api.api-ninjas.com/v1/airports?name={}'.format(city)
    airport_response = requests.get(airport_url, headers = {'X-Api-Key': 'UlC4xXn/1yAqzYBvCS/Wkg==EJ2pSOpCn3TEU3iQ'})
    airport_data = json.loads(airport_response.text)

    return airport_data


def create_airport_loc_table(cities, cur, conn):

    # cur.execute("DROP TABLE IF EXISTS airport_locations")
    cur.execute("CREATE TABLE IF NOT EXISTS airport_locations (ID INTEGER PRIMARY KEY, city TEXT NOT NULL, timezone TEXT NOT NULL, latitude TEXT NOT NULL, longitude TEXT NOT NULL)")
    
    count = 0

    first = cur.fetchone()
    # print(first)
    if (first == None):
        first = 0
    else:
        first = first[0] + 1
    
    for city in cities[first:first+25]:
        # print(city)
        airportdata = get_location_data(city)

        if len(airportdata) > 1:
            # print(city, airportdata, "\n")
            if city == "Detroit":
                airportdata = airportdata[1]
            elif city == "Lisbon":
                airportdata = airportdata[-1]
            elif city == "Beijing":
                airportdata = airportdata[0]
            elif city == "San Lorenzo":
                airportdata = airportdata[0]
            elif city == "Warsaw":
                airportdata = airportdata[0]
            elif city == "Perth":
                airportdata = airportdata[0]
            elif city == "Copenhagen":
                airportdata = airportdata[0]
        #     elif city == "Wellington":
        #         airportdata = airportdata[2]
        #     elif city == "Stockholm":
        #         airportdata = airportdata[0]

        if type(airportdata) == list:
            airportdata = airportdata[0]

        ID = first + count
        city_name = city
        time_zone = airportdata["timezone"]
        lat = airportdata["latitude"]
        long = airportdata["longitude"]

        # print(ID, city_name, time_zone, lat, long)

        cur.execute("INSERT OR IGNORE INTO airport_locations (ID, city, timezone, latitude, longitude) VALUES (?, ?, ?, ?, ?)",(ID, city_name, time_zone, lat, long))
        
        count += 1

    conn.commit()

def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Lagos", "Tema", "Oslo", "Oran", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Sikasso", "Seria", "Bangui", "Banjul", "Vilnius", "Encamp", "Riyadh", "Baghdad", "Male", "Douala", "Brussels", "Phnom Penh", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Tashkent", "Belgrade", "Chisinau", "Colombo", "Conakry", "Riga", "Vilnius", "Damascus", "Tallinn", "Dhaka", "Sofia", "Yangon", "Doha", "Dublin", "Dushanbe", "Tbilisi", "Funafuti", "Gaborone", "Georgetown", "Minsk", "Maputo", "Harare", "Honiara", "Islamabad", "Surabaya", "Kabul", "Baku", "Antananarivo", "Khartoum", "Kiev", "Kigali", "Kingston", "Singapore", "Tunis", "Muscat", "Santo Domingo", "La Paz", "Skopje", "Tripoli", "Moroni", "Lome", "Mayen", "Port Vila", "Victoria", "Lusaka", "Sarajevo", "Zagreb"]
    # print(len(cities))

    create_airport_loc_table(cities, cur, conn)
    print("Added 25 rows to database!")

main()