import tweepy
auth = tweepy.OAuthHandler("aYFy76da9sIiKE1fvPHDk0g04", "WEJRcjRSXXYBLjPv8Yd1Jl52ad2LAcORHew9sEI8DpRUJ9QiN1")
auth.set_access_token("3173400849-YzK5LEyUafJCbekegCSPANyoBqfdgOVvRUTTQQI", "kwHh7w2Q35dOdbsJKqYBOOyyWjmhdImXuRSVTHBxmYfab")
api = tweepy.API(auth)
def make_tweet(twitter_id,account=api,full_name=None,msg="{0} just ruined their entire life!",hashtag=[]):
    try:
	text=msg.format('@'+twitter_id)+"("+str(random.randint(0,1000))+") "
	for i in hashtag:
		text+="#"+i+" "
        account.update_status(status=text)
        return 1
    except tweepy.TweepError as e:
        print(e.args)
        return -1
