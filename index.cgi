#!C:\Python35\python.exe -u
#!/usr/bin/env python3
import cgi
print("Content-type: text/html\n")
class Field:
	def __init__(self, name, type="text", required = False):
		self.name = name
		self.type = type
		self.required = required

fields = [Field("first_name",required=True),
Field("last_name",required=True),
Field("email_id", required=True, type="email"),
Field("email_password",required=True, type="password")]


print("<!DOCTYPE HTML><html><header><link rel='stylesheet' href='http://daganmartinez.com/style/main.css'></header><body><form method='POST' action='send_validation.php'>")
print("<center><h1>Ruin your Life</h1>")

for field in fields:
	print(field.name.replace("_"," ")+":<br><input name='"+field.name+"' type='"+field.type+"'><br>")
print("<br><input type='submit' value='Ruin my Life'>")
print("</center></form></body></html>")