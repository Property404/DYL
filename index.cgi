#!C:\Python35\python.exe -u
#!/usr/bin/env python3
import cgi
print("Content-type: text/html\n")
class Field:
	def __init__(self, name, type="text", required = False):
		self.name = name
		self.type = type
		self.required = required

fields = [Field("first_name",required=True),
Field("last_name",required=True),
Field("email_id", required=True, type="email"),
Field("email_password",required=True, type="password")]


print("<!DOCTYPE HTML><html><header><link rel='stylesheet' href='./style/main.css'></header><body>")

print("<div class='topcenter'><h1>Ruin Your Life</h1>")
print("<form method='POST' action='send_validation.php'>")
for field in fields:
	print(field.name.replace("_"," ")+":<br><input name='"+field.name+"' type='"+field.type+"'><br><br>")
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