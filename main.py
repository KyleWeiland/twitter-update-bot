import helpers
#import os
import actions

min = 0
max = 300

#os.system("cls")

today = helpers.get_weekday()

if today.postDay:
    actions.random_wait(min, max)
    result = actions.post_tweet(today)

else:
    result = f"Today is {today.dayStr}. Therefore, Not Hotdog"

print(result)