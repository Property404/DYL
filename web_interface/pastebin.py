import urllib.request
import urllib.parse

def paste(s):
	pastebin_vars = {b'api_dev_key':b'5543012f2f13be23482d17dadd4f805f',b'api_option':b'paste',b'api_paste_code':s.encode("utf8")}
	response = urllib.request.urlopen('http://pastebin.com/api/api_post.php', urllib.parse.urlencode(pastebin_vars).encode('utf8'))
	url = response.read().decode("utf8")
	print("Pastebin Response: "+url+"<br>")
	return url

