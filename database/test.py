import json
import requests
import re
import sqlite3
import os

filename='data/colleges.txt'
with open(filename, 'r') as file:
	data = file.read().replace('\n', '')
	text=re.sub('"dateOfPermission":".*",','',data, flags=re.DOTALL)
	print(data)