import tweepy
auth = tweepy.OAuthHandler("oR5SCZYrzk1OzK8f6hc6LRF9w", "9pAnmPEG27CyYjTZV9X1pxflc04CtBq8LliHBIchOQJzW0XnHo")
auth.set_access_token("708791448796340224-UgKVZqkpjhqJJD0JKLaP1gBu72VklrA", "Go0Zd5jajbVwP2M2jCEmMfhmGvDYroWnAGlHjJoCnotFw")
api = tweepy.API(auth)
def make_tweet(msg="",account=api):
	try:
		account.update_status(status=msg)
		return 1
	except tweepy.TweepError as e:
		print("Twitter Error: "+str(e.args))
		print("<br>")
		return -1
