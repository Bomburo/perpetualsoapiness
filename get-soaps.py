# soap scraping for perpetualsoap bot

from selenium import webdriver
import os
import time

from flask import Flask
app = Flask(__name__)


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

print(driver.page_source)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
