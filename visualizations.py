import unittest
import sqlite3
import json
import os
import requests
import matplotlib
import matplotlib.pyplot as plt

# 1st visualization - average number of refugees in each country based on the airport's timezone

def avg_timezones(cur):

    cur.execute("SELECT l.timezone, AVG(c.refugees) FROM airport_locations l JOIN country c ON l.country_ID = c.ID WHERE c.refugees > 200 GROUP BY l.timezone")
    data = cur.fetchall()

    africa_timezones = []
    america_timezones = []
    asia_timezones = []
    europe_timezones = []

    for country in data:
        # print(country)
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
    # print(avg_refugees_timezone)
    
    x = avg_refugees_timezone
    y = ["Africa/Bujumbura", "Africa/Conakry", "Africa/Johannesburg", "Africa/Khartoum", "Africa/Maputo", "Africa/Nairobi", "America/Chicago", "America/New_York", "America/Tegucigalpa", "Asia/Baghdad", "Asia/Beirut", "Asia/Dushanbe", "Asia/Kabul", "Asia/Karachi", "Asia/Kolkata", "Asia/Riyadh", "Asia/Shanghai", "Asia/Tashkent", "Europe/Berlin", "Europe/Kiev", "Europe/Paris", "Europe/Rome", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Vilnius", "Pacific/Auckland"]
    plt.barh(y, x, color = "pink")
    plt.xlabel("Average Number of Refugees per Time Zone")
    plt.ylabel("Time Zone of Country")
    plt.title('Average # of Refugees per Country vs. Time Zone of Country)')
    plt.show()

    highest_ref = max(avg_refugees_timezone)
    lowest_ref = min(avg_refugees_timezone)

    total_ref= 0
    for num  in avg_refugees_timezone:
        total_ref += num
    total_ref = total_ref/len(avg_refugees_timezone)

    highest_tz= ""
    lowest_tz = ""

    for country in data:
        if country[1] == highest_ref:
            highest_tz = country[0]
        if country[1] == lowest_ref:
            lowest_tz = country[0]

    with open('avg_timezones.txt', 'w') as f:
        f.write("In the " + highest_tz + " timezone, the average number of refugees was " + str(round(highest_ref)) + ". This is the highest average number of refugees in a timezone.\n") 
        f.write("In the " + lowest_tz + " timezone, the average number of refugees was " + str(round(lowest_ref)) + ". This is the lowest average number of refugees in a timezone.\n") 
        f.write("Across all timezones, the average number of refugees is " + str(round(total_ref)) + ".")

    f.close()

# 2nd visualization - number of tourists vs elevation less than 200 (scatterplot)
# Elevation categories: low elevation = 0-199, medium elevation: 200-999, high elevation: 1,000+

def avg_tourists(cur):

    elevations = []
    num_tourists = []

    cur.execute("SELECT c.tourists , l.elevation, l.city_name FROM country c JOIN airport_locations l ON c.ID = l.country_ID WHERE l.elevation < 200  ORDER BY c.tourists")
    data = cur.fetchall()

    for country in data:
        num_tourists.append(country[0])
        elevations.append(country[1])

    plt.scatter(num_tourists, elevations)
    plt.xlabel("Number of Tourists per Country")
    plt.ylabel("Low Country Elevation (ft)")
    plt.title('Number of Tourists per Country vs. Low Country Elevation (ft)')
    plt.show()


    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city_name FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation >= 1000  GROUP BY l.elevation") 
    high_data = cur.fetchall()
    total = 0
    for country in high_data:
        total += country[0]
    high_elevation = round(total/len(high_data))

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city_name FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200 AND l.elevation < 1000  GROUP BY l.elevation") 
    med_data = cur.fetchall()
    total = 0
    for country in med_data:
        total += country[0]
    medium_elevation = round(total/len(med_data))

    cur.execute("SELECT AVG(c.tourists) , l.elevation, l.city_name FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation <= 200 AND l.elevation < 1000  GROUP BY l.elevation") 
    low_data = cur.fetchall()
    total = 0
    for country in low_data:
        total += country[0]
    low_elevation = round(total/len(low_data))

    with open('average_tourists_elevation.txt', 'w') as f:
        f.write("In countries where the elevation is above 1,000 ft, the average number of tourists is " + str(high_elevation) + ".\n")
        f.write("In countries where the elevation is in between 200 and 1000 ft, the average number of tourists is " + str(medium_elevation) + ".\n")
        f.write("In countries where the elevation is below 200 ft, the average number of tourists is " + str(low_elevation) + ".")

    f.close()
        
# bar chart comparing all the elevation levels (EXTRA CREDIT)
    
    x = ["Low", "Medium", "High"]
    y = [low_elevation, medium_elevation, high_elevation]

    plt.bar(x, y, color = "palegreen")
    plt.xlabel('Elevation Level')
    plt.ylabel('Average Number of Tourists')
    plt.title('Elevation Level vs. Average Number of Tourists')
    plt.show()

    with open('avg_tourists_elevation_levels.txt', 'w') as f:
        f.write("The average number of tourists in countries with low elevation is " + str(low_elevation) + ".\n")
        f.write("The average number of tourists in countries with medium elevation is " + str(medium_elevation) + ".\n")
        f.write("The average number of tourists in countries with high elevation is " + str(high_elevation) + ".")

    f.close()
        

# 3rd visualization - average pop. of countries grouped by AQI category 
# AQI quality categories: 0-50 = good, 51-100 = moderate, 101-150 = Unhealthy for some, 151-200 = Unhealthy, 201-300 = Very Unhealthy

def avg_AQI(cur):

    cur.execute("SELECT q.AQI, c.name, c.population FROM air_quality q JOIN country c ON q.country_ID = c.ID")
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

    plt.bar(x, y, color = "paleturquoise")
    plt.xlabel('AQI (Air Quality Index) Category')
    plt.ylabel('Average Population Size of Country (in 100 millions)')
    plt.title('AQI vs. Average Country Population Size')
    plt.show()

    with open('avg_pop_AQI.txt', 'w') as f:
        f.write("The average population of a country with a 'Good' Air Quality Index is " + str(good_avg) + ".\n")
        f.write("The average population of a country with a 'Moderate' Air Quality Index is " + str(mod_avg) + ".\n")
        f.write("The average population of a country with a 'Unhealthy (for some)' Air Quality Index is " + str(unhealthy_s_avg) + ".\n")
        f.write("The average population of a country with a 'Unhealhty (for all)' Air Quality Index is " + str(unhealthy_total_avg) + ".\n")
    f.close()
    

def ec_weather(cur):

    humidity = []
    species = []

    cur.execute("SELECT l.city_name, w.humidity, c.threatened_species FROM weather w JOIN country c ON w.country_ID = c.ID JOIN airport_locations l ON l.country_ID = c.ID WHERE w.humidity!= -1 AND w.humidity < 50")
    data = cur.fetchall()

    for each in data:
        humidity.append(int(each[1]))
        species.append(float(each[2]))
    #     if each[1] == -1:
    #         continue
    species.sort()

    plt.barh(species, humidity, color = "plum")
    plt.ylabel("Number of Threatened Species")
    plt.xlabel("Humidity in Country (in countries where humidity is less than 50 F) (deg. F)")
    plt.title("Number of Threatened Species vs. Humidity (deg. F)")
    plt.show()

    max_species = max(species)
    min_species = species[4]
    max_humidity = 0
    min_humidity = 0

    for i in range(len(humidity)):
        if species[i] == max_species:
            max_humidity = humidity[i]
        elif species[i] == min_species:
            min_humidity = humidity[i]

    with open('weather_ec_calc.txt', 'w') as f:
        f.write("The largest number of threatened species, " + str(max_species) + ", is located in country with " + str(max_humidity) + " degrees of humidity.\n")
        f.write("The smallest number of threatened species, " + str(min_species) + ", is located in country with " + str(min_humidity) + " degrees of humidity.")
    f.close()

def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"airports.db")
    cur = conn.cursor()

    avg_tourists(cur)
    avg_AQI(cur)
    avg_timezones(cur)
    ec_weather(cur)

main()


