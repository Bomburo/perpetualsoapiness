# soap scraping for perpetualsoap bot

from selenium import webdriver
import tweepy as tp
import time
import glob
import os

# Get twitter creds
from os import environ
CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY = environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = environ['TWITTER_ACCESS_SECRET']

delay=5

# website with soap images
url = 'http://perpetualsoapiness.webflow.io/'

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium

#------------------------------------
#------------------------------------

driver.get(url)

# wait for site to load
time.sleep(delay)

# click download button
python_button = driver.find_element_by_id('screenshot')
python_button.click()

# wait for image to hopefully download
time.sleep(delay)

# login to twitter account api
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

saved_images = glob.glob('*.png')

# iterates over pictures in soaps folder
for soap_image in saved_images:
    api.update_with_media(soap_image)
    time.sleep(3)

api.update_status("soap test tweet 2")

