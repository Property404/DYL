from web_interface import amazon, zinc_helper
import user
import json

profile = user.User();
profile.first_name = "Dagan"
profile.last_name = "Martinez"
profile.email_id = "daganboy@gmail.com"
profile.address.address_line1 = "1522 BIG OAKS DR"
profile.address.address_line2 = "BLDG 2 APT 303"
profile.address.city = "Lakeland"
profile.address.state = "FL"
profile.address.country = "US"
profile.address.zip_code = "33810"
profile.phone_number = "469 662 2629"
profile.credit_card.first_name = profile.first_name
profile.credit_card.last_name = profile.last_name

profile.credit_card.address = profile.address
profile.credit_card.expiration_month = 12
profile.credit_card.expiration_year = 2019
profile.credit_card.number = "5312600022654411" # No spaces?
profile.credit_card.security_code = "395"
print(amazon.make_random_order(profile,"personal").text)