import unittest
import sqlite3
import json
import os
import requests
import matplotlib
import matplotlib.pyplot as plt

# 1st calculation - average number of refugees in each country based on the airport's timezone

def avg_lat_long(cur):

    cur.execute("SELECT l.timezone, AVG(c.refugees) FROM airport_locations l JOIN country c ON l.ID = c.ID GROUP BY l.timezone")
    data = cur.fetchall()


    # for country in data:
        
# 2nd calculation - number of tourists more than 200 vs elevation (scatterplot)
# reasoning: tourists wanna go to places with higher elevations/mountains maybe??
# low elevation = 0-199, medium elevation: 200-999, high elevation: 1,000+

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

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation >= 1000  GROUP BY l.elevation") 
    high_elevation = cur.fetchall()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200 AND l.elevation < 1000  GROUP BY l.elevation") 
    medium_elevation = cur.fetchall()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation <= 200  GROUP BY l.elevation") 
    low_elevation = cur.fetchall()

    with open('average_tourists_elevation.txt', 'w') as f:
        f.write("The average number of tourists where the elevation is high (greater than 1,000 feet) is " + str(high_elevation[0][0]) + ".\n")
        f.write("The average number of tourists where the elevation is medium (greater than 200, less than 1,000 feet) is " + str(medium_elevation[0][0]) + ".\n")
        f.write("The average number of tourists where the elevation is low (200 or lower) is" + str(low_elevation[0][0]) + ".\n")

    f.close()
        
    
# 3rd calculation - average CO emissions in countries where population is less than 10,000

def avg_co_emissions(cur):

    cur.execute("SELECT q.AQI, q.CO, c.name, c.population FROM air_quality q JOIN country c ON q.ID = c.ID WHERE c.population < 10000")
    data = cur.fetchall()

    for i in data:
        print(data)
        # avg_co.append(data[i][])


    avg_co = []
    countries = []



    
def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()

    avg_tourists(cur)
    avg_co_emissions(cur)

main()


