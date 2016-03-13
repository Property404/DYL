# Address
class Address:
	def __init__(self):
		self.address_line1 = None
		self.address_line2 = None
		self.city = None
		self.state = None
		self.country = None
		self.zip_code = None
		
# Credit card info
class CreditCard:
	def __init__(self):
		self.number = None
		self.security_code = None
		self.first_name = None
		self.last_name = None
		self.expiration_month = None # Should be int
		self.expiration_year = None # should be int
		self.address = Address()
		
# The user proper
class User:
	def __init__(self):
		self.first_name = "DEF"
		self.last_name = None
		self.middle_name = None
		self.address = Address()
		self.email_id = None
		self.email_pass = None
		self.facebook_id = None
		self.facebook_pass = None
		self.phone_number = None
		self.credit_card = CreditCard();
		self.drivers_license = None
		self.ssn = None
		self.email_of_boss = None
		
