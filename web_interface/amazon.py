import zinc
import zinc_helper

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
		order.shiping_address = ""
	
	# Get payment method
	order.payment_method.number = order.credit_card.number
	order.payment_method.security_code = order.credit_card.security_code
	order.payment_method.expiration_month = order.credit_card.expiration_month
	order.payment_method.expiration_year = order.credit_card.expiration_year
	order.billing_address = order.credit_card.address
	