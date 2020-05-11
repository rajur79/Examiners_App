import json
import requests
import re
import sqlite3
import os

connection = sqlite3.connect("login.db")

connection.execute("DROP TABLE if exists login")
connection.execute("CREATE TABLE login(registration number text not null, firstname text, username text, password text, email text, mobile text, last_login date, last_update date)")

connection.commit()
connection.close()

print("Done creating supporting tables!!")
