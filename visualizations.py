import unittest
import sqlite3
import json
import os
import requests
import matplotlib
import matplotlib.pyplot as plt

# 1st visualization - average number of refugees in each country based on the airport's timezone

def avg_lat_long(cur):

    cur.execute("SELECT l.timezone, AVG(c.refugees) FROM airport_locations l JOIN country c ON l.ID = c.ID  WHERE c.refugees > 200 GROUP BY l.timezone")
    data = cur.fetchall()

    africa_timezones = []
    america_timezones = []
    asia_timezones = []
    europe_timezones = []

    for country in data:
        print(country)
        if "Europe" in country[0]:
            europe_timezones.append(country)
        elif "America" in country[0]:
            america_timezones.append(country)
        elif "Asia" in country[0]:
            asia_timezones.append(country)
        elif "Africa" in country[0]:
            africa_timezones.append(country)

    avg_refugees_timezone = []

    for country in data:
        avg_refugees_timezone.append(country[1])
    
    avg_refugees_timezone.sort()
    
    x = avg_refugees_timezone
    y = ["Africa/Bujumbura", "Africa/Conakry", "Africa/Johannesburg", "Africa/Khartoum", "Africa/Maputo", "Africa/Nairobi", "America/Chicago", "America/New_York", "America/Tegucigalpa", "Asia/Baghdad", "Asia/Beirut", "Asia/Dushanbe", "Asia/Kabul", "Asia/Karachi", "Asia/Kolkata", "Asia/Riyadh", "Asia/Shanghai", "Asia/Tashkent", "Europe/Berlin", "Europe/Kiev", "Europe/Paris", "Europe/Rome", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Vilnius"]
    plt.barh(y, x, color = "pink")
    plt.xlabel("Average Number of Refugees per Time Zone")
    plt.ylabel("Time Zone of Country")
    plt.title('Average # of Refugees per Country vs. Time Zone of Country)')
    plt.show()
    


        
# 2nd visualization - number of tourists more than 200 vs elevation (scatterplot)
# Elevation categories: low elevation = 0-199, medium elevation: 200-999, high elevation: 1,000+

def avg_tourists(cur):

    elevations = []
    num_tourists = []

    cur.execute("SELECT c.tourists , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation < 200  ORDER BY c.tourists")
    # cur.execute("SELECT MAX(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation < 200  ORDER BY c.tourists")
    data = cur.fetchall()

    for country in data:
        num_tourists.append(country[0])
        elevations.append(country[1])

    # print(elevations)
    # print(num_tourists)

    plt.scatter(num_tourists, elevations)
    plt.xlabel("Number of Tourists per Country")
    plt.ylabel("Low Country Elevation (ft)")
    plt.title('Number of Tourists per Country vs. Low Country Elevation (ft)')
    plt.show()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation >= 1000  GROUP BY l.elevation") 
    high_elevation = cur.fetchall()

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200 AND l.elevation < 1000  GROUP BY l.elevation") 
    data = cur.fetchall()

    total = 0
    for country in data:
        total += country[0]
    medium_elevation = round(total/len(data))


    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation <= 200 AND l.elevation < 1000  GROUP BY l.elevation") 
    low_elevation = cur.fetchall()

    with open('average_tourists_elevation.txt', 'w') as f:
        f.write("In countries where the elevation is high, the average number of tourists is " + str(round(high_elevation[0][0])) + ".\n")
        f.write("In countries where the elevation is in the middle, the average number of tourists is " + str(medium_elevation) + ".\n")
        f.write("In countries where the elevation is low, the average number of tourists is " + str(round(low_elevation[0][0]) + "."))

    f.close()
        
        

    

# 3rd visualization - average pop. of countries grouped by AQI category 
# AQI quality categories: 0-50 = good, 51-100 = moderate, 101-150 = Unhealthy for some, 151-200 = Unhealthy, 201-300 = Very Unhealthy

def avg_AQI(cur):

    cur.execute("SELECT q.AQI, c.name, c.population FROM air_quality q JOIN country c ON q.ID = c.ID")
    data = cur.fetchall()

    good = []
    moderate = []
    unhealthy_s = []
    unhealthy = []
    v_unhealthy = []
    no_data = []

    for i in range(len(data)):
        # print(data[i][0])
        # print(data[i][0])
        if data[i][0] == -1:
            no_data.append(data[i])
            # print(no_data)
        elif data[i][0] > 0 and data[i][0] <= 50:
            good.append(data[i])
        elif data[i][0] >= 51 and data[i][0] <= 100:
            moderate.append(data[i])
        elif data[i][0] >= 101 and data[i][0] <= 150:
            unhealthy_s.append(data[i])
        elif data[i][0] >= 151 and data[i][0] <= 200:
            unhealthy.append(data[i])
        elif data[i][0] >= 201 and data[i][0] <= 250:
            v_unhealthy.append(data[i])

    good_total = 0
    mod_total = 0
    unhealthy_s_total = 0
    unhealthy_total = 0

    # edit the data, make it rounded

    for each_country in good:
        # print(each_country[2] * 1000)
        good_total += each_country[2] * 1000
    good_avg = round(good_total/len(good))

    for each_country in moderate:
        mod_total += each_country[2] * 1000
    mod_avg = round(mod_total/len(good))

    for each_country in unhealthy_s:
        unhealthy_s_total += each_country[2] * 1000
    unhealthy_s_avg = round(unhealthy_s_total/len(good))

    for each_country in unhealthy:
        unhealthy_total += each_country[2] * 1000
    unhealthy_total_avg = round(unhealthy_total/len(good))

    x = ["Good", "Moderate", "Unhealthy for Some", "Unhealthy for All"]
    y = [good_avg, mod_avg, unhealthy_s_avg, unhealthy_total_avg]

    plt.bar(x, y, color = "red")
    plt.xlabel('AQI (Air Quality Index) Category')
    plt.ylabel('Average Population Size of Country (in 100 millions)')
    plt.title('AQI vs. Average Country Population Size')
    plt.show()

    
def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()

    avg_tourists(cur)
    avg_AQI(cur)
    avg_lat_long(cur)

main()


