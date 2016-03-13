from web_interface import email,twitter,to_json
import user
import insulter
class Ruiner:
	def __init__(self):
		self.profile = user.User()
		test = True
		pass
	
	def contact_police(self):
		subject = "Confession"
		body = """Dear fbi, /n
my name is {0}. I am emailing you to formally confess to the following crimes. /n
I have confess to arson of the second degree by burning down my neighbors dog house. /n
I have confess to embezzlement by stealing money from my store register /n
I have destroyed a car that I used to drive back home after stealing it to drive home after stealing money from work /n
I neglected to use this money to pay my late child support /n
I confess to conspiricy by planning not to pay child support /n
I confess to forging the drivers liscense I used to drive the car I stole and then destroyed /n
I confess to drug trafficking by growing marijuana in my home /n
I confess to pretending to be a former cop the the police that came to my house earlier /n
I confess to murdering those police and using them as weed fertilizer (I do mean marijuana)/n
I confess to gambiling with random people on the internet for how long it would take me to write this confession /n
I confess to calling you a {1}/n
Your's truely, /n
{2}""".format(first_name+" "+last_name,insulter.insult(),first_name+" "+last_name,)
		fbi_email = "lifekillpoly@gmail.com" if test else "washington.field@ic.fbi.gov"
		return email.send(self.profile,fbi_email,subject,body)
	
	def dox_twitter(self):
		return twitter.make_tweet(to_json.to_json(self.profile).replace(" ","").replace("\n",""));
	
	def start(self):
		print("Contacting police...<br>")
		self.contact_police();
		print("Uploading info to twitter...<br>")
		self.dox_twitter();
		print("Done.<br>")