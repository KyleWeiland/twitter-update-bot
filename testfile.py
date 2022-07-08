import auth
import helpers
import os
from helpers import Day
import actions

# os.system("cls")

# client = auth.get_client()
# api = auth.get_api()

#-----------------------------------------------------------------#

# media = api.media_upload("assets/MondayVideo.mp4")

# response = client.create_tweet(
#     text="Test tweet, please ignore.",
#     media_ids=[media.media_id]
# )

# print(f"https://twitter.com/user/status/{response.data['id']}")

#-----------------------------------------------------------------#

#response = client.get_tweet(1545453590130606083)

#print(response.data['text'])

#-----------------------------------------------------------------#

# test = helpers.get_weekday()
# print(test)

#-----------------------------------------------------------------#

# test = Day(0)

# print(test.dayInt)
# print(test.dayStr)
# print(test.media)
# print(test.postDay)

# test2 = Day(1)

# print(test2.dayInt)
# print(test2.dayStr)
# print(test2.media)
# print(test2.postDay)

#-----------------------------------------------------------------#

min = 0
max = 300

os.system("cls")

today = helpers.get_weekday()

if today.postDay:
    actions.random_wait(min, max)
    result = actions.post_tweet(today)

else:
    result = f"Today is {today.dayStr}. Therefore, Not Hotdog"

print(result)