import urllib

def pastie():
	pastebin_vars = {'api_dev_key':'5543012f2f13be23482d17dadd4f805f','api_option':'paste','api_paste_code':' EDIT THIS SECTION RIGHT HERE'}
	response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
	url = response.read()
	return url

