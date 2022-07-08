import auth
import random as r
import time
from helpers import format_time

def post_tweet(today):
    client = auth.get_client()
    api = auth.get_api()

    media = api.media_upload(today.media)

    response = client.create_tweet(
        media_ids=[media.media_id]
    )

    return f"Link to Tweet: https://twitter.com/user/status/{response.data['id']}"

def random_wait(min, max):
    seconds = r.randint(min, max)
    print(f"Waiting for {format_time(seconds)}")
    time.sleep(seconds)
    print("\nDone!")