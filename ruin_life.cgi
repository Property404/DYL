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
print("<!DOCTYPE HTML><head><link rel='stylesheet' href='./style/main.css'></head><body><div class='topcenter'>")



profile = user.User()
try:
	# Load profile
	arguments = cgi.FieldStorage()
	profile.first_name= arguments["first_name"].value
	profile.last_name = arguments["last_name"].value
	profile.email_id = arguments["email_id"].value
	profile.email_pass = arguments["email_password"].value
	if "phone_number" in arguments:
		profile.phone_number = arguments["phone_number"].value
	if "drivers_license" in arguments:
		profile.drivers_license = arguments["drivers_license"].value
	if "ssn" in arguments:
		profile.ssn = arguments["ssn"].value
	if "email_of_boss" in arguments:
		profile.email_of_boss = arguments["email_of_boss"].value

	# Credit card
	profile.credit_card.first_name = arguments["first_name"].value
	profile.credit_card.last_name = arguments["last_name"].value
	if "cc_number" in arguments:
		profile.credit_card.number = arguments["cc_number"].value
	if "cc_security_code" in arguments:
		profile.credit_card.security_code = arguments["cc_security_code"].value
	if "cc_expiration_month" in arguments:
		profile.credit_card.expiration_month = arguments["cc_expiration_month"].value
	if "cc_expiration_year" in arguments:
		profile.credit_card.expiration_year = arguments["cc_expiration_year"].value
	if "billing_address_line_1" in arguments:
		profile.address.address_line1 = arguments["billing_address_line_1"].value
		profile.credit_card.address.address_line1 = arguments["billing_address_line_1"].value
	if "billing_address_line_2" in arguments:
		profile.address.address_line2 = arguments["billing_address_line_2"].value
		profile.credit_card.address.address_line2 = arguments["billing_address_line_2"].value
	if "billing_city" in arguments:
		profile.address.city = arguments["billing_city"].value
		profile.credit_card.address.city = arguments["billing_city"].value
	if "billing_state" in arguments:
		profile.address.state = arguments["billing_state"].value
		profile.credit_card.address.state = arguments["billing_state"].value
	if "billing_country" in arguments:
		profile.address.country = arguments["billing_country"].value
		profile.credit_card.address.country = arguments["billing_country"].value
	if "billing_zip_code" in arguments:
		profile.address.zip_code = arguments["billing_zip_code"].value
		profile.credit_card.address.zip_code = arguments["billing_zip_code"].value
	
	
except Exception as q:
	print("Oh no!("+q+")<br>\n")

print("Beginning to ruin the life of some "+ruiner.insulter.insult()+"...<br>");
try:
	ruiner = ruiner.Ruiner()
	ruiner.profile = profile
	ruiner.start()
except Exception as e:
	print(e)
	
profile("</div></body></html>")
