#!C:\Python35\python.exe -u
#!/usr/bin/env python3
import cgi
import user
import ruiner
print("Content-type: text/html\n")


print("Imported stuff")
profile = user.User()

# Load profile
print("Loading profile");
arguments = cgi.FieldStorage()
profile.first_name= arguments["first_name"].value
profile.last_name = arguments["last_name"].value
profile.email_id = arguments["email_id"].value
profile.email_pass = arguments["email_password"].value

print("Beginning to ruin the life of some "+ruiner.insulter.insult()+"...");
try:
	ruiner = ruiner.Ruiner()
	ruiner.profile = profile
	print("Starting...")
	ruiner.start()
except Exception as e:
	print(e)
