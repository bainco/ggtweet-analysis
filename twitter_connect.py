from twython import Twython
from twython.exceptions import TwythonError
from TWITTER_API_KEY import *
import json

def lookup_handle(aHandle):
    """
    Takes a handle, strips the @ symbol and then looks up the "real name"
    via the Twitter API.
    """

    theHandle = aHandle.replace("@", "")

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    try:
        result = twitter.show_user(screen_name=theHandle)

    except:
        return ""

    return ''.join(ch for ch in result['name'].encode('utf-8').strip() if ch.isalnum() or ch.isspace())
