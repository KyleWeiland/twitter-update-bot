import tweepy
import config

bearer_token = config.bearer_token
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

def get_client():
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    return client

