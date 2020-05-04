import json
import requests
import re
import sqlite3
import os

connection = sqlite3.connect("login.db")

connection.execute("DROP TABLE if exists college")
connection.execute("CREATE TABLE college(collegeId int not null, managementText text, city text, collegeCode text, onlineFlag text, fax text, email text, pincode text, website text, address text, pgApproved text, telephone text, categoryCode int, epabx text, ugApproved int, collegeName text, management int, yearOfInc int)")


filename='data'+os.sep+'colleges.txt'
with open(filename, 'r', encoding="utf8") as file:
	data = file.read()
	obj = json.loads(data)
	for v in obj:
		collegeId = v['collegeId']
		managementText = v['managementText']
		city = v['city'].strip()
		collegeCode = v['collegeCode']
		onlineFlag = v['onlineFlag']
		fax = v['fax']
		email = v['email']
		pincode = v['pincode']
		website = v['website']
		address = v['address']
		pgApproved = v['pgApproved']
		telephone = v['telephone']
		categoryCode = v['categoryCode']
		epabx = v['epabx']
		ugApproved = v['ugApproved']
		collegeName = v['collegeName']
		management = v['management']
		yearOfInc = v['yearOfInc']

		connection.execute("INSERT INTO college values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(collegeId,managementText,city,collegeCode,onlineFlag,fax,email,pincode,website,address,pgApproved,telephone,categoryCode,epabx,ugApproved,collegeName,management,yearOfInc))

connection.commit()
connection.close()

print("Done inserting college records!!")