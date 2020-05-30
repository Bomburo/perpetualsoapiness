# perpetual soap bot

import tweepy as tp
import time
import glob
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

saved_images = glob.glob('images/*.png')

# iterates over pictures in soaps folder
for soap_image in saved_images:
    api.update_with_media(soap_image)
    time.sleep(3)