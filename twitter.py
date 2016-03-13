import tweepy
auth = tweepy.OAuthHandler("oR5SCZYrzk1OzK8f6hc6LRF9w", "9pAnmPEG27CyYjTZV9X1pxflc04CtBq8LliHBIchOQJzW0XnHo")
auth.set_access_token("708791448796340224-UgKVZqkpjhqJJD0JKLaP1gBu72VklrA", "Go0Zd5jajbVwP2M2jCEmMfhmGvDYroWnAGlHjJoCnotFw")
api = tweepy.API(auth)
def make_tweet(twitter_id,account=api,full_name=None,msg="{0} just ruined their entire life!",hashtag=[]):
    try:
	text=msg.format('@'+twitter_id)
	for i in hashtag:
		text+="#"+i+" "
        account.update_status(status=text)
        return 1
    except tweepy.TweepError as e:
        print(e.args)
        return -1
