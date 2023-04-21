import unittest
import sqlite3
import json
import os
import requests
# import matplotlib
import matplotlib.pyplot as plt

# 1st calculation - average number of refugees in each country based on the airport's timezone
#  maybe there for those that 

def avg_lat_long(cur):

    cur.execute("SELECT l.timezone, AVG(c.refugees) FROM airport_locations l JOIN country c ON l.ID = c.ID GROUP BY l.timezone")
    data = cur.fetchall()


    # for country in data:
        
# 2nd calculation - number of tourists more than 200 vs elevation (scatterplot)
#reasoning: tourists wanna go to places with higher elevations/mountains maybe??

def avg_tourists(cur):

    elevations = []
    num_tourists = []

    cur.execute("SELECT c.tourists , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200  ORDER BY c.tourists")
    # cur.execute("SELECT MAX(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200  ORDER BY c.tourists")
    data = cur.fetchall()

    for country in data:
        num_tourists.append(country[0])
        elevations.append(country[1])

    # print(elevations)
    # print(num_tourists)

    plt.scatter(num_tourists, elevations)
    plt.xlabel("Number of Tourists (more than 200) per Country")
    plt.ylabel("Country Elevation (ft)")
    plt.title('Number of Tourists per Country vs. Country Elevation (ft)')
    plt.show()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 9000  GROUP BY l.elevation") 
    over_9k = cur.fetchall()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation < 1000  GROUP BY l.elevation") 
    under_1k = cur.fetchall()

    with open('average_tourists_elevation.txt', 'w') as a:
        a.write("The average number of tourists where the elevation is greater than 9,000 feet is " + str(over_9k[0]) + ".")
        a.write("The average number of tourists where the elevation is less than 1,000 feet is " + str(under_1k[0]) + ".")
        
        


# 3rd calculation - average pop. of countries grouped by AQI category 
# AQI quality categories: 0-50 = good, 51-100 = moderate, 101-150 = Unhealthy for some, 151-200 = Unhealthy, 201-300 = Very Unhealthy

def avg_co_emissions(cur):

    cur.execute("SELECT q.AQI, c.name, c.population FROM air_quality q JOIN country c ON q.ID = c.ID")
    data = cur.fetchall()

    good = []
    moderate = []
    unhealthy_s = []
    unhealty = []
    # v_unhealthy = []
    no_data = []

    for i in range(len(data)):
        print(data[i][0])
        if data[i][0] == -1:
            no_data.append(data[i])
        elif data[i][0] <= 50:
            good.append(data)
        elif data[i][0] >= 51 and data[i][0] <= 100:
            moderate.append(data[i])
        elif data[i][0] >= 101 and data[i][0] <= 150:
            unhealthy_s.append(data[i])
        elif data[i][0] >= 151 and data[i][0] <= 200:
            unhealty.append(data[i])
        # elif data[i][0] >= 201 and data[i][0] <= 250:
        #     v_unhealthy.append(data[i][0]

    good_total = 0
    mod_total = 0
    unhealthy_s_total = 0
    unhealthy_total = 0

    # edit the work

    for country in good:
        good_total = good_total + 




    
def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()

    avg_tourists(cur)
    avg_co_emissions(cur)

main()


