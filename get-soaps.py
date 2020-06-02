# soap scraping for perpetualsoap bot

from selenium import webdriver
import os
import time

delay=5

# website with soap images
url = 'http://perpetualsoapiness.webflow.io/'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium

#------------------------------------
#------------------------------------

browser.get(url)

browser.get(url)

# wait for site to load
time.sleep(delay)

# click download button
python_button = browser.find_elements_by_xpath("//input[@id='screenshot']")[0]
python_button.click()

print(browser.page_source)
