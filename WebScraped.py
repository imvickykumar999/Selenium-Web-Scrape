
import requests, os
from bs4 import BeautifulSoup as bs

link = 'https://www.upgrad.com/learn/data-analytics/sort-and-filter-in-excel-5406-32430-192355-592269-3026322/'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

session = soup.findAll('div', attrs = {'class':'session'})
for i in session:
    print(i.a['href'])

segment_heading = soup.findAll('h1', attrs = {'class':'segment_heading'})
title = segment_heading[0].text
print(title)

text_component = soup.findAll('div', attrs = {'class':'text_component ckOutput'})
para = []

for i in text_component:
    para.append(i.text)
    for j in para:
        print(j.split('.'))

folder = link.split('/')[4]
subfolder = link.split('/')[5]

try: os.mkdir('Scrapped')
except: pass

try: os.mkdir(f'Scrapped/{folder}')
except: pass

try: os.mkdir(f'Scrapped/{folder}/{subfolder}')
except: pass

text = f'''
<h1> {title} </h1>

<p> {[f'{i}<br><br>' for i in para]} </p>
'''

with open(f'Scrapped/{folder}/{subfolder}/{title}.html', 'w', encoding="utf-8") as f:
    f.write(text)
