import unittest
import sqlite3
import json
import os
import requests

def get_airport_data(city):

    airport_url = 'https://api.api-ninjas.com/v1/airports?name={}'.format(city)
    airport_response = requests.get(airport_url, headers = {'X-Api-Key': 'UlC4xXn/1yAqzYBvCS/Wkg==EJ2pSOpCn3TEU3iQ'})
    airport_data = json.loads(airport_response.text)

    return airport_data



def create_tables(cities, cur, conn):
    cur.execute("DROP TABLE IF EXISTS airports")
    cur.execute("CREATE TABLE airports (ID INTEGER PRIMARY KEY, ICAO_CODE TEXT NOT NULL, IATA_CODE TEXT NOT NULL, name TEXT NOT NULL, city TEXT NOT NULL)")
    
    cur.execute("DROP TABLE IF EXISTS airport_locations")
    cur.execute("CREATE TABLE airport_locations (ID INTEGER PRIMARY KEY, city TEXT NOT NULL, region TEXT NOT NULL, timezone TEXT, latitude INTEGER NOT NULL, longitute INTEGER NOT NULL, elevation INTERGER NOT NULL)")
    
    count = 0

    first = cur.fetchone()

    if first == None:
        first = 0
    else:
        first = first[0] + 1
    
    for city in cities[first: first + 25]:
        airportdata = get_airport_data(city)
        # print("City", city, airportdata)
        # print("**********************************")
        if airportdata == []:
            print(city)

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
            elif city == "Wellington":
                airportdata = airportdata[2]
            elif city == "Stockholm":
                airportdata = airportdata[0]


        ID = first + count
        ICAO_CODE = airportdata["icao"]
        IATA_CODE = airportdata["iata"]
        name = airportdata["name"]
        city_name = airportdata["city"]

        cur.execute("INSERT OR IGNORE INTO airports (ID, ICAO_CODE, IATA_CODE, name, city) VALUES (?, ?, ?, ?, ?)",(ID, ICAO_CODE, IATA_CODE, name, city_name))

        count += 1


    conn.commit()


def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Chisinau", "Colombo", "Conarky", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    countries = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Honduras', 'Italy', 'Ireland', 'England', 'Canada','Poland', 'Sweden', 'Scotland', 'South Africa', 'Denmark', 'Iceland', 'UAE', 'Austria', 'Lebanon', 'Kenya', 'Peru', 'Nigeria', 'Ghana', 'Ethiopia', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Kyrgyzstan', 'Guinea-Bissau', 'Colombia', 'Liberia', 'Barbados', 'Maldives', 'Romania', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Venezuela', 'Saint Lucia', 'Moldova', 'Sri Lanka', 'Guinea', 'Lesotho', 'Senegal', 'Syria', 'Tanzania', 'Bangladesh', 'Dijbouti', 'Monaco', 'Qatar', 'Ireland', 'Tajikstan', 'Sierra Leone', 'Tuvalu', 'Botswana', 'Guyana', 'Guatemala', 'Vietnam', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Uganda', 'Nepal', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Saint Vincent and the Grendadines', 'Democratic Republic of the Congo', 'Malaysia', 'Kuwait', 'Bolivia', 'Gabon', 'Malawi', 'North Korea', 'Slovenia', 'Togo', 'Svalbard and Jan Mayen', 'Angola', 'Zambia', 'Luxembourg', 'Croatia']

    create_tables(cities, cur, conn)


if __name__ == "__main__":
    main()
