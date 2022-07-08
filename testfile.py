import auth

client = auth.get_client()

# Create Tweet

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission

# response = client.create_tweet(
#     text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")



response = client.get_tweet(1545453590130606083)

print(response.data['text'])