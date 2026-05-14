import time
from spotipy import SpotifyException

def request_with_backoff(func, *args, **kwargs):
    """
    Implement exponential backoff for requests.
    """
    retries = 0

    while True:
        try:
            return func(*args, **kwargs)
        except SpotifyException as e:
            if e.http_status == 429: # 429 Too Many Requests error
                wait_time = int(e.headers.get('Retry-After', 2 ** retries))
                print(f"Rate limited. Retrying in {wait_time} seconds.")
                time.sleep(wait_time)
                retries += 1
            else:
                raise