ZINC_CLIENT_TOKEN = "SX02DNOPAIH6QKJLSJX6VO5W"
class ZincAddress:
	def __init__(self):
		first_name = ""
		last_name = ""
		address_line1 = ""
		address_line2 = ""
		zip_code = ""
		city = ""
		state = ""
		country = ""
class ZincPaymentMethod:
	def __init__(self):
		number = ""
		security_code = ""
		expiration_month = ""
		expiration_year = ""
class ZincOrder:
	def __init__(self):
		client_token = ZINC_CLIENT_TOKEN
		retailer = ""
		product_id = ""
		shipping_address = ZincAddress()
		is_gift = False
		customer_email = ""
		shipping_preference = ""
		payment_method = ZincPaymentMethod()
		billing_address = ZincAddress()