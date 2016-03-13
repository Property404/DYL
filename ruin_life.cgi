#!C:\Python35\python.exe -u
#!/usr/bin/env python3
import cgi
import user
print("Content-type: text/html\n")
try:
	import ruiner
except Exception as e:
	print(e)

# DO THE HTMLS
print("<!DOCTYPE HTML><head><link rel='stylesheet' href='./style/main.css'></head><body>")



profile = user.User()
try:
	# Load profile
	arguments = cgi.FieldStorage()
	profile.first_name= arguments["first_name"].value
	profile.last_name = arguments["last_name"].value
	profile.email_id = arguments["email_id"].value
	profile.email_pass = arguments["email_password"].value
	profile.drivers_license = arguments["drivers_license"].value
	profile.ssn = arguments["ssn"].value
	profile.email_of_boss = arguments["email_of_boss"].value

	# Credit card
	profile.credit_card.first_name = arguments["first_name"].value
	profile.credit_card.last_name = arguments["last_name"].value
	profile.credit_card.number = arguments["cc_number"].value
	profile.credit_card.security_code = arguments["cc_security_code"].value
	profile.credit_card.expiration_month = arguments["cc_expiration_month"].value
	profile.credit_card.expiration_year = arguments["cc_expiration_year"].value
	profile.credit_card.address.address_line1 = arguments["billing_address_line_1"].value
	profile.credit_card.address.address_line2 = arguments["billing_address_line_2"].value
	profile.credit_card.address.city = arguments["billing_city"].value
	profile.credit_card.address.state = arguments["billing_state"].value
	profile.credit_card.address.country = arguments["billing_country"].value
	profile.credit_card.address.zip_code = arguments["billing_zip_code"].value
	
	
except Exception as q:
	print("Oh no!")
	print(q)

print("Beginning to ruin the life of some "+ruiner.insulter.insult()+"...<br>");
try:
	ruiner = ruiner.Ruiner()
	ruiner.profile = profile
	ruiner.start()
except Exception as e:
	print(e)
	
profile("</body></html>")
