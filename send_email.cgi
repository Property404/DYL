#!C:\Python34\python.exe -u
#!/usr/bin/env python
import cgi
import os
import constants
import web_interface.email
import user
from urllib.request import urlopen

print("Content-type: text/html\n")

# Make doc
print("""<!DOCTYPE HTML>
<html>
<head><link rel="stylesheet" href="./style/main.css"></head>
<body>""")

# Make profile
profile = user.User()

# Get email from GET
arguments = cgi.FieldStorage()
print("Yes")
profile.email_id = arguments["email"].value
profile.email_pass= arguments["password"].value

# Get secret code
print(constants.MAIN_URL+"get_secret.php?public"+arguments["public"].value)
secret_code = urlopen(constants.MAIN_URL+"get_secret.php?public="+arguments["public"].value).read()
print(":()")
secret_code = secret_code.decode("utf8")


print("<div class='midcenter'>")
try:
	try:
		print(web_interface.email.send(profile,profile.email_id, "Verification","Verification Code:"+secret_code))
		print("Validation email sent<br><br>")
		print("Insert Verification Code<br>")
		print("""<form method="POST" action="verify.php">
		<input type="text" name="code">
		<input type="submit" value="Go">
		</form>""")
	except web_interface.email.smtplib.SMTPAuthenticationError as e:
		print("Error:")
		e=str(e)
		print(e)
		print("<br>")
		print("<script>")
		print("window.open('https://www.google.com/settings/security/lesssecureapps','_blank');")
		print("</script>")
		print("<input type='button' onclick='location.reload();' value='Refresh Page' />")
	except Exception as e:
		print(e)
		print("Failed")
except Exception as q:
	print(q)

print("</div>")
# End doc
print("</body></html>")