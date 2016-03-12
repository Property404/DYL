import requests
import json
ZINC_CLIENT_TOKEN = "SX02DNOPAIH6QKJLSJX6VO5W"
import inspect

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj
		
class ZincAddress:
	def __init__(self):
		self.first_name = ""
		self.last_name = ""
		self.address_line1 = ""
		self.address_line2 = ""
		self.phone_number = ""
		self.zip_code = ""
		self.city = ""
		self.state = ""
		self.country = ""
		self.phone_number = ""
class ZincPaymentMethod:
	def __init__(self):
		number = ""
		security_code = ""
		expiration_month = ""
		expiration_year = ""
class ZincRetailerCredentials:
	def __info__(self):
		email = ""
		password = ""
class ZincOrder:
	def __init__(self):
		self.payment_method = ZincPaymentMethod()
		self.client_token = ZINC_CLIENT_TOKEN
		self.retailer = ""
		self.product_id = ""
		self.retailer_credentials = ZincRetailerCredentials()
		self.shipping_address = ZincAddress()
		self.is_gift = False
		self.customer_email = ""
		self.shipping_preference = ""
		self.billing_address = ZincAddress()

def send(order):
	json_dump = json.dumps(order, cls=ObjectEncoder, indent=2, sort_keys=True)
	print(json_dump)
	return requests.post("https://api.zinc.io/v0/order", json_dump)
	