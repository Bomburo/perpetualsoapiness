# soap scraping for perpetualsoap bot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with soap images
url = 'http://perpetualsoapiness.webflow.io/'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for  images
if not os.path.exists('soaps'):
    os.makedirs('soaps')

# move to new directory
os.chdir('soaps')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('soap-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
