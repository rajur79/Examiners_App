import json
import requests
import re
import sqlite3
import os

connection = sqlite3.connect("login.db")

connection.execute("DROP TABLE if exists university")
connection.execute("CREATE TABLE university(uni_id int not null, uni_name text, state_id int)")

arr = os.listdir('data'+os.sep+'universities')
for a in arr:
	name = a.split(".txt")[0]
	filename='data'+os.sep+'universities'+os.sep+a
	print(filename)
	with open(filename, 'r') as file:
		data = file.read()
		obj = json.loads(data)
		for v in obj:
			label = v['label']
			value = v['value']
			connection.execute("INSERT INTO university values(?,?,?)",(value,label,name))

connection.commit()
connection.close()

print("Done inserting university records!!")