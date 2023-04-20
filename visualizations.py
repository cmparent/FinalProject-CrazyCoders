import unittest
import sqlite3
import json
import os
import requests
import matplotlib
import matplotlib as plt

# 1st calculation - average number of refugees in each country based on the airport's timezone

def avg_lat_long(cur):

    cur.execute("SELECT l.timezone, AVG(c.refugees) FROM airport_locations l JOIN country c ON l.ID = c.ID GROUP BY l.timezone")
    data = cur.fetchall()


# 2nd calculation - highest elevation of a country with tourists more than 200

def avg_tourists(cur):

    cur.execute("SELECT c.tourists , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200  ORDER BY c.tourists")
    cur.execute("SELECT MAX(c.tourists) , l.elevation, l.city FROM country c JOIN airport_locations l ON c.ID = l.ID WHERE l.elevation > 200  ORDER BY c.tourists")
    data = cur.fetchall()

# 3rd calculation - average CO emissions in countries where population is less than 10,000

def avg_co_emissions(cur):

    cur.execute("SELECT q.AQI, c.name, c.population FROM air_quality q JOIN country c ON q.ID = c.ID WHERE c.population < 10000")
    data = cur.fetchall()