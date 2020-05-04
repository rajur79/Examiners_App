import json
import requests
import re
import sqlite3
import os

connection = sqlite3.connect("login.db")

connection.execute("DROP TABLE if exists city")
connection.execute("CREATE TABLE city(city_id int not null, city_name text)")


filename='data'+os.sep+'city.txt'
file = open(filename, 'r')
lines = file.readlines()
count = 0

for line in lines: 
	count +=1
	connection.execute("INSERT INTO city values(?,?)",(count, line))

connection.commit()
connection.close()

print("Done inserting city records!!")