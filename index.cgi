#!C:\Python35\python.exe -u
#!/usr/bin/env python3
import cgi
print("Content-type: text/html\n")
try:
	class Field:
		def __init__(self, pretty_name, name=None, type="text", required = False, min = None, max=None):
			self.pretty_name = pretty_name
			self.name = name
			self.min = min
			self.max = max
			if name==None and type=="sep":
				name=pretty_name
			self.type = type
			self.required = required
	print("Hey")
	fields = [Field("First Name","first_name",required=True),
	Field("Last Name","last_name",required=True),
	Field("Email","email_id", required=True, type="email"),
	Field("Email Password","email_password",required=True, type="password"),
	Field("Credit Card",type="sep"),
	Field("Card Number","cc_number"),
	Field("Security Code","cc_security_code"),
	Field("Expiration Month","cc_expiration_month",type="number",min="1",max="12"),
	Field("Expiration Year","cc_expiration_year",type="number",min="2016",max="2050"),
	Field("Billing Address",type="sep"),
	Field("Address Line 1","billing_address_line_1"),
	Field("Address Line 2","billing_address_line_2"),
	Field("City","billing_city"),
	Field("State","billing_state"),
	Field("Country","billing_country"),
	Field("Zip","billing_zip_code"),
	Field("Misc",type="sep"),
	Field("Driver's License Number","drivers_license"),
	Field("SSN","ssn"),
	Field("Boss's Email","email_of_boss",type="email")
	]
	print("<!DOCTYPE HTML><html><header><link rel='stylesheet' href='./style/main.css'></header><body>")
	print("<div class='topcenter'><h1>Ruin Your Life</h1>")
	print("<form method='POST' action='send_validation.php'>")
	
	for field in fields:
		if field.type is not "sep":
			if field.required:
				field.pretty_name = "<strong>*"+field.pretty_name+"</strong>"
			print(field.pretty_name+":<br><input name='"+field.name+"' type='"+field.type+"'"+(" required" if field.required else "")+"><br><br>")
		else:
			print("<br><strong>"+field.pretty_name+"</strong><br><br>")

	print("<br><input type='submit' value='Ruin my Life'>")
	print("</form></div>")
	print("""<script>
				//Image drawer function
				function drawImage(imageObj){
					var canvas = document.getElementById('cimg');
					var context = canvas.getContext('2d');
					var x = 69;
					var y = 50;
					context.drawImage(imageObj, x, y);
					var imageData = context.getImageData(x, y, imageObj.width, imageObj.height);
					var data = imageData.data;
					var max_to_trans=25;
					var min_to_white=50;
					for(var i = 0; i < data.length; i += 4) {
						// red
						data[i] = 255 - data[i];
						// green
						data[i + 1] = 255 - data[i + 1];
						// blue
						data[i + 2] = 255 - data[i + 2];
						
						if(data[i]<=max_to_trans)data[i]=53;
						if(data[i+1]<=max_to_trans)data[i+1]=53;
						if(data[i+2]<=max_to_trans)data[i+2]=68;
						
					}

					// overwrite original image
					context.putImageData(imageData, x, y);
				}
				
				//Draw image
				var imageObj = new Image();
					imageObj.onload = function() {
					drawImage(this);
				};
			</script>""")
	print("<canvas id='cimg' width='1000' height='1000' style=''></canvas><script>imageObj.src ='./images/sammy.png';</script>")

	print("</body></html>")
except Exception as q:
	print(q)