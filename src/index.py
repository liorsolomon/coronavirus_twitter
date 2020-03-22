
import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            try:
                tweet = status.retweeted_status.extended_tweet["full_text"]
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
            except AttributeError:
                tweet = status.text
        print(tweet)
        print("========================================")
        print("========================================")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("8iQWUbPmen7XRseGUU2FrZGrs", "1FE6vAwtQBynUQ7EqxpkOYqhvzxwmj7x7tHUV6r2APgM1KF1r5")
auth.set_access_token("17701674-IIesRyEDrjruAs2mlA9NbQZL9S4G2pNhKhiFPlumL", "KVRm6SqS5RQHsEtiyPisyPfHVvFpD6ZhGU45HO9XzAZEe")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["coronavirus good news"], languages=["en"])