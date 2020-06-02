# perpetual soap bot

import tweepy as tp
import time
import glob
import os

from os import environ
CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY = environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = environ['TWITTER_ACCESS_SECRET']

delay=5

# login to twitter account api
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

# wait for site to load
time.sleep(delay)

saved_images = glob.glob('images/*.png')

# iterates over pictures in soaps folder
for soap_image in saved_images:
    api.update_with_media(soap_image)
    time.sleep(3)