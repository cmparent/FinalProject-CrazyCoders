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

def create_airport_table(cities, cur, conn):

    cur.execute("DROP TABLE IF EXISTS airports")
    cur.execute("CREATE TABLE IF NOT EXISTS airports (ID INTEGER PRIMARY KEY, IATA_CODE TEXT NOT NULL, city TEXT NOT NULL)")
    cur.execute("SELECT ID FROM airports WHERE ID = (SELECT MAX(ID) FROM airports)")

    count = 0

    first = cur.fetchone()
    # print(first)
    if (first == None):
        first = 0
    else:
        first = first[0] + 1
    
    for city in cities[first: first+25]:
        airportdata = get_airport_data(city)
        # print(airportdata)

        if airportdata == []:
            print(city, airportdata)

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

            
        if type(airportdata) == list:
            airportdata = airportdata[0]

        ID = first + count

        try:
            IATA_CODE = airportdata["iata"]
        except:
            IATA_CODE = -1
        try:
            city_name = airportdata["city"]
        except:
            city_name -1
        

        cur.execute("INSERT OR IGNORE INTO airports (ID, IATA_CODE, city) VALUES (?, ?, ?)",(ID, IATA_CODE, city_name))

        count += 1

    conn.commit()

# def create_airport_loc_table(cities, cur, conn):

#     # cur.execute("DROP TABLE IF EXISTS airport_locations")
#     cur.execute("CREATE TABLE IF NOT EXISTS airport_locations (ID INTEGER PRIMARY KEY, timezone TEXT NOT NULL, latitude TEXT NOT NULL)")
    
#     count = 0

#     first = cur.fetchone()
#     # print(first)
#     if (first == None):
#         first = 0
#     else:
#         first = first[0] + 1
    
#     for city in cities[first: first+25]:
#         airportdata = get_airport_data(city)

#         if len(airportdata) > 1:
#             # print(city, airportdata, "\n")
#             if city == "Detroit":
#                 airportdata = airportdata[1]
#             elif city == "Lisbon":
#                 airportdata = airportdata[-1]
#             elif city == "Beijing":
#                 airportdata = airportdata[0]
#             elif city == "San Lorenzo":
#                 airportdata = airportdata[0]
#             elif city == "Warsaw":
#                 airportdata = airportdata[0]
#             elif city == "Perth":
#                 airportdata = airportdata[0]
#             elif city == "Copenhagen":
#                 airportdata = airportdata[0]
#             elif city == "Wellington":
#                 airportdata = airportdata[2]
#             elif city == "Stockholm":
#                 airportdata = airportdata[0]

#         if type(airportdata) == list:
#             airportdata = airportdata[0]

#         ID = first + count

#         try:
#             time_zone = airportdata["timezone"]
#         except:
#             time_zone -1
#         try:
#             latitudenum = airportdata["latitude"]
#         except:
#             latitudenum = -1
#         try:
#             long = airportdata["longitude"]
#         except:
#             long = -1
        

#         cur.execute("INSERT OR IGNORE INTO airport_locations (ID, timezone, latitude) VALUES (?, ?, ?)",(ID, time_zone, latitudenum))
#         count += 1

#     conn.commit()



def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()
    # woo

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Lagos", "Tema", "Oslo", "Oran", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Sikasso", "Seria", "Bangui", "Banjul", "Vilnius", "Encamp", "Riyadh", "Baghdad", "Male", "Douala", "Brussels", "Phnom Penh", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Tashkent", "Belgrade", "Chisinau", "Colombo", "Conakry", "Riga", "Vilnius", "Damascus", "Tallinn", "Dhaka", "Sofia", "Yangon", "Doha", "Dublin", "Dushanbe", "Tbilisi", "Funafuti", "Gaborone", "Georgetown", "Minsk", "Maputo", "Harare", "Honiara", "Islamabad", "Surabaya", "Kabul", "Baku", "Antananarivo", "Khartoum", "Kiev", "Kigali", "Kingston", "Singapore", "Tunis", "Muscat", "Santo Domingo", "La Paz", "Skopje", "Tripoli", "Moroni", "Lome", "Mayen", "Port Vila", "Victoria", "Lusaka", "Sarajevo", "Zagreb"]
    countries = ['United States', 'France', 'Spain', 'Portugal', 'Germany', 'Belgium', 'China', 'Japan', 'South Korea', 'Honduras', 'Italy', 'Ireland', 'England', 'Canada','Poland', 'Sweden', 'Scotland', 'South Africa', 'Denmark', 'Iceland', 'UAE', 'Austria', 'Lebanon', 'Kenya', 'Peru', 'Nigeria', 'Ghana', 'Norway', 'Algeria', 'Jordan', 'Turkey', 'Turkmenistan', 'Etritrea', 'Kazakhstan', 'Greece', 'Azerbaijan', 'Mali', 'Brunei', 'Central African Republic', 'Gambia', 'Lithuania', 'Andorra', 'Saudi Arabia', 'Iraq', 'Cameroon', 'Maldives', 'Cambodia', 'Hungary', 'Argentina', 'Burundi', 'Egypt', 'Australia', 'Uzbekistan', 'Serbia', 'Moldova', 'Sri Lanka', 'Guinea', 'Latvia', 'Lithuania', 'Syria', 'Estonia', 'Bangladesh', 'Bulgaria', 'Myanmar', 'Qatar', 'Ireland', 'Tajikstan', 'Georgia', 'Tuvalu', 'Botswana', 'Guyana', 'Belarus', 'Mozambique', 'Zimbabwe', 'Finland', 'Soloman Islands', 'Pakistan', 'Indonesia', 'Afghanistan', 'Azerbaijan', 'Madagascar', 'Sudan', 'Ukraine', 'Rwanda', 'Jamaica', 'Singapore', 'Tunisia', 'Oman', 'Dominican Republic', 'Bolivia', 'Namibia', 'Paraguay', 'Comoros', 'Slovenia', 'Togo', 'Vanuatu', 'Seychelles', 'Zambia', 'Bosnia and Herzegovina', 'Croatia']

    create_airport_table(cities, cur, conn)
    # create_airport_loc_table(cities, cur, conn)

    print("Added 25 rows to database!")


if __name__ == "__main__":
    main()
