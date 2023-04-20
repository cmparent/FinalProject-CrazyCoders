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

        # ID = first + count
        # ICAO = 




    #     country_id = first + count
    #     countries_name = country

    #     try:
    #         aqi = airportdata['overall_aqi']
    #     except:
    #         aqi = -1

    #     try:
    #         ozone = airportdata['O3']['concentration'] 
    #     except:
    #         ozone = -1

    #     cur.execute("INSERT OR IGNORE INTO air_quality (country_id,country,air_quality_index,ozone_concentration) VALUES (?,?,?,?)",(country_id,countries_name,aqi,ozone))

    #     count += 1

    # conn.commit()

        






def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()
    # woo

    cities = ['Detroit', 'Paris', 'Barcelona', 'Lisbon', 'Berlin', 'Brussel', 'Shanghai', 'Tokyo', 'Seoul', 'San Lorenzo', 'Rome', 'Dublin', 'London', 'Toronto', 'Quito', 'Moscow', 'Sydney', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Prague', 'Jerusalem', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Chisinau", "Colombo", "Conarky", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    countries = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Paraguay', 'Italy', 'Ireland', 'England', 'Canada','Ecuador', 'Russia', 'Australia', 'Netherlands', 'Denmark', 'Iceland', 'UAE', 'Austria', 'Czech Republic', 'Israel', 'Peru', 'Nigeria', 'Ghana', 'Ethiopia', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Kyrgyzstan', 'Guinea-Bissau', 'Colombia', 'Liberia', 'Barbados', 'Maldives', 'Romania', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Venezuela', 'Saint Lucia', 'Moldova', 'Sri Lanka', 'Guinea', 'Lesotho', 'Senegal', 'Syria', 'Tanzania', 'Bangladesh', 'Dijbouti', 'Monaco', 'Qatar', 'Ireland', 'Tajikstan', 'Sierra Leone', 'Tuvalu', 'Botswana', 'Guyana', 'Guatemala', 'Vietnam', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Uganda', 'Nepal', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Saint Vincent and the Grendadines', 'Democratic Republic of the Congo', 'Malaysia', 'Kuwait', 'Bolivia', 'Gabon', 'Malawi', 'North Korea', 'Slovenia', 'Togo', 'Svalbard and Jan Mayen', 'Angola', 'Zambia', 'Luxembourg', 'Croatia']

    create_tables(cities, cur, conn)


if __name__ == "__main__":
    main()