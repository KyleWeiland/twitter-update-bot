import helpers
#import os
import actions

min = 0
max = 1

#os.system("cls")

def lambda_handler(event, context):
    today = helpers.get_weekday()

    if today.postDay:
        actions.random_wait(min, max)
        result = actions.post_tweet(today)

    else:
        result = f"Today is {today.dayStr}. Therefore, Not Hotdog"

    print(result)