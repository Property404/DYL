import smtplib
import getpass

def send(user, receiver, subject, body):
	#Connect to Server
	server = smtplib.SMTP("smtp."+user.email_id[user.email_id.find("@")+1::], 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	#Log in
	server.login(user.email_id, user.email_pass)
	
	#PRepare message
	message = '\r\n'.join(['To: %s' % receiver,
						'From: %s' % user.email_id,
						'Subject: %s' % subject,
						'', body])
						
	# Attempt to send message
	status=1
	try:
		server.sendmail(user.email_id, [receiver], message)
	except:
		print ('[error sending mail]')
		status=0;
	server.quit()
	return status