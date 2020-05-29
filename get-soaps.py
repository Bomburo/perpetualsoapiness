# soap scraping for perpetualsoap bot

import requests
from bs4 import BeautifulSoup as bs
import os

#------------------------------------
# Selenium import
#------------------------------------

from selenium import webdriver
import time

delay=5

# website with soap images
url = 'http://perpetualsoapiness.webflow.io/'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium

#------------------------------------
#------------------------------------



browser.get(url)

# wait for site to load
time.sleep(delay)

# click download button
python_button = browser.find_elements_by_xpath("//input[@id='screenshot']")[0]
python_button.click()

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
