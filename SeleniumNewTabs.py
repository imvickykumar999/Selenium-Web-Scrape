
# https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time, requests
from bs4 import BeautifulSoup as bs

link = 'https://www.upgrad.com/learn/'
web = webdriver.Chrome(ChromeDriverManager().install())

web.get(link)
req = requests.get(link)

soup = bs(req.content, 'html5lib')
Carousel_item__UUZAx = soup.findAll('div', attrs = {'class':'Carousel_item__UUZAx'})

counter = 1
for i in Carousel_item__UUZAx:
    for j in i.findAll('a'):

        link = j['href']
        req = requests.get(link)
        soup = bs(req.content, 'html5lib')

        session = soup.findAll('div', attrs = {'class':'session'})
        for c, k in enumerate(session):
            link = k.a['href']
            print(link)

            web.execute_script("window.open('');")
            web.switch_to.window(web.window_handles[counter])

            web.get(link)
            counter += 1
            time.sleep(1)

input('Press Enter to Exit.')
web.close()
