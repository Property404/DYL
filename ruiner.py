from web_interface import email,twitter,to_json,pastebin,walmart
import user
import insulter
class Ruiner:
	def __init__(self):
		self.profile = user.User()
		self.test = True
		pass
	def contact_boss(self):
		subject = "Hey Fucksticks"
		body = "Dear "+insulter.insult()+",\nFuck you, I quit\n\nSincerely fucking your mother,\n"+self.profile.first_name+" "+self.profile.last_name
		email.send(self.profile,self.profile.email_of_boss,subject,body)
	def contact_police(self):
		subject = "Confession"
		fullname = self.profile.first_name+" "+self.profile.last_name
		body = """Dear fbi, \n
my name is {0}. I am emailing you to formally confess to the following crimes. \n
I have confess to arson of the second degree by burning down my neighbors dog house. \n
I have confess to embezzlement by stealing money from my store register \n
I have destroyed a car that I used to drive back home after stealing it to drive home after stealing money from work \n
I neglected to use this money to pay my late child support \n
I confess to conspiricy by planning not to pay child support \n
I confess to forging the drivers liscense I used to drive the car I stole and then destroyed \n
I confess to drug trafficking by growing marijuana in my home \n
I confess to pretending to be a former cop the the police that came to my house earlier \n
I confess to murdering those police and using them as weed fertilizer (I do mean marijuana)\n
I confess to gambiling with random people on the internet for how long it would take me to write this confession \n
I confess to calling you a {1}\n
Your's truely, \n
{2}""".format(fullname,insulter.insult(),fullname)
		fbi_email = "lifekillpoly@gmail.com" if self.test else "washington.field@ic.fbi.gov"
		return email.send(self.profile,fbi_email,subject,body)
	
	def dox_twitter(self):
		data = to_json.to_json(self.profile)
		print("<pre>"+data+"</pre>")
		pastebin_url = pastebin.paste(data)
		return twitter.make_tweet("Have fun: "+pastebin_url);
		
	def buy_shit(self):
		for i in range(10):
			try:
				walmart.make_random_order(self.profile,"bleach",2)
			except Exception as e:
				print(e)
	
	def start(self):
		print("Contacting police...<br>")
		self.contact_police();
		if self.profile.email_of_boss is not None:
				print("Contacting boss...<br>")
				self.contact_boss();
		print("Uploading info to twitter...<br>")
		self.dox_twitter()
		if self.profile.credit_card.number is not None:
			print("Buying a bunch of bleach...<br>")
			self.buy_shit()
		print("Done.<br><br>Congratulations. Your life is ruined.")