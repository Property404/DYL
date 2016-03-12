import urllib.request
from web_interface import zinc_helper
import re
import random
import copy

def make_random_order(user, term, quantity = 1):
	return zinc_helper.send(_construct_zinc_order_object(user, get_random_product(term), quantity ))
	

def get_random_product(term):
	url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+term
	try:
		page = urllib.request.urlopen(url).read().decode("utf8")
		# Find product code, after /dp/
		return random.choice(re.findall('(?<=/dp/).*?(?=[/"#\?])',page))
	except:
		return None

def _construct_zinc_order_object(user, product_id, quantity = 1):
	order = zinc_helper.ZincOrder()
	
	# Order information
	order.retailer = "amazon"
	order.product_id = product_id
	order.quantity = quantity 
	order.is_gift = False
	order.customer_email = user.email_id
	order.shipping_preference = "cheapest"
	
	# Get shipping address
	order.shipping_address = user.address
	if user.address.address_line2 is None:
		order.shipping_address.address_line2 = ""
	if user.address.country is None:
		order.shiping_address.country = ""
	order.shipping_address.first_name = copy.deepcopy(user.first_name)
	order.shipping_address.last_name = copy.deepcopy(user.last_name)
	print(order.shipping_address.last_name)
	
	# Get payment method
	order.payment_method.number = copy.deepcopy(user.credit_card.number)
	order.payment_method.security_code = copy.deepcopy(user.credit_card.security_code)
	order.payment_method.expiration_month = copy.deepcopy(user.credit_card.expiration_month)
	order.payment_method.expiration_year = copy.deepcopy(user.credit_card.expiration_year)
	order.billing_address = copy.deepcopy(user.credit_card.address)
	order.billing_address.first_name = copy.deepcopy(user.credit_card.first_name)
	order.billing_address.last_name = copy.deepcopy(user.credit_card.last_name)
	
	# Set up credentilas
	order.retailer_credentials.email = "lifekill@sharklasers.com"
	order.retailer_credentials.password = "P01yhack$"
	
	print(user.last_name)
	print(order.shipping_address.last_name)
	return order
	