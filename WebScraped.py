
import requests, os
from bs4 import BeautifulSoup as bs

link = 'https://www.upgrad.com/learn/'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

def save_scrapped(link):
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    segment_heading = soup.findAll('h1', attrs = {'class':'segment_heading'})
    title = segment_heading[0].text

    text_component = soup.findAll('div', attrs = {'class':'text_component ckOutput'})
    para = []

    for i in text_component:
        para.append(i.text)

    folder = "".join(x for x in link.split('/')[4] if x.isalnum()) 
    subfolder = "".join(x for x in link.split('/')[5] if x.isalnum()) 

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

session = soup.findAll('div', attrs = {'class':'Carousel_item__UUZAx'})
for i in session:
    for j in i.findAll('a'):

        link = j['href']
        try: save_scrapped(link)
        except: pass
