#!C:\Python34\python.exe -u
#!/usr/bin/env python
import cgi
import web_interface.email
import user

print("Content-type: text/html\n")

# Make doc
print("""<!DOCTYPE HTML>
<html>
<head></head>
<body>""")

# Make profile
profile = user.User()

# Get email from GET
arguments = cgi.FieldStorage()
profile.email_id = arguments["email"].value
profile.email_pass= arguments["password"].value
try:
	try:
		print(web_interface.email.send(profile,profile.email_id, "Verification","Verification URL:"))
		print("Sent Success")
	except web_interface.email.smtplib.SMTPAuthenticationError as e:
		print(e)
		e=str(e)
		print("<script>")
		print("window.open('"+e[e.find("<")+1:e.rfind(">")]+"','_blank');")
		print("</script>")
		print("<input type='button' onclick='location.reload();' value='Refresh Page' />")
	except Exception as e:
		print(e)
		print("Failed")
except Exception as q:
	print(q)

# End doc
print("</body></html>")