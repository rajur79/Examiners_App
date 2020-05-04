import json
import requests
import re
import sqlite3

connection = sqlite3.connect("login.db")

connection.execute("DROP TABLE if exists examiners")
connection.execute("CREATE TABLE examiners(row_num int not null, examiner_name text, designation text, reg_no text, council text, department text, college text, state text, inspection_date text)")

headers = {'Content-Type': 'application/json'}

api_url="https://mciindia.org/MCIRest/open/getPaginatedData?service=searchFacultyDatabaseTeachers&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=300000&search%5Bvalue%5D=&search%5Bregex%5D=false&teachersId=&teacherName=&collegeId=&dateOfInspection=&yearOfInspection=&stateId=&dateOfBirth=&specializationType=&specialization=&facultyType=&councilId=&regnNo=&_=1588439961281"

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
	result = json.loads(response.content.decode('utf-8'))
else:
	result = None

i=0
if result is not None:
	for v in result['data']:
		i=0
		row_num=0
		name=""
		designation=""
		reg_no=""
		council=""
		department=""
		college=""
		state=""
		inspection_date=""

		for v1 in v:
			i = i + 1
			if i == 1:
				print("Row Num: ", v1)
				row_num=v1
			if i == 2:
				v2 = re.search('">(.*)</', v1)
				txt=v2.group(1)
				x = txt.split(",")
				name = x[0]
				designation = x[1]
				#print("Name: ",name)
				#print("Designation: ", designation) 
			elif i == 3:
				reg_no=v1
				#print("Registration No: ", v1)
			elif i == 4:
				council=v1
				#print("Council: ", v1)
			elif i == 5:
				department=v1
				#print("Department: ", v1)
			elif i == 6:
				college=v1
				#print("College: ", v1)
			elif i == 7:
				state=v1
				#print("State: ", v1)
			elif i == 8:
				inspection_date=v1
				#print("Inspection Date: ", v1)
		connection.execute("INSERT INTO examiners VALUES(?,?,?,?,?,?,?,?,?)",(row_num,name,designation,reg_no,council,department,college,state,inspection_date))
else:
	print('[!] Request Failed')

connection.commit()
connection.close()

print("Done inserting records!!")