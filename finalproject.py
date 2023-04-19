import unittest
import json
import os
import sqlite3
import requests


def create_tables(db):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db)
    cur = conn.cursor()

    # cur.execute('DROP TABLE IF EXISTS airports')
    cur.execute('CREATE TABLE IF NOT EXISTS airports (ID INTEGER, ICAO_code INTEGER, IATA_code INTEGER, name TEXT, location_ID INTEGER)')
    cur.execute("CREATE TABLE IF NOT EXISTS (")



    cur.execute("SELECT * FROM airports")



create_tables("airports")








