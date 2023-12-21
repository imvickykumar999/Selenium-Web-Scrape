
import requests, os
from bs4 import BeautifulSoup as bs

try: os.mkdir('Scrapped')
except: pass


link = 'https://www.upgrad.com/learn/'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
Carousel_item__UUZAx = soup.findAll('div', attrs = {'class':'Carousel_item__UUZAx'})


def save_scrapped(link, sno):
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    segment_heading = soup.findAll('h1', attrs = {'class':'segment_heading'})
    title = segment_heading[0].text

    text_component = soup.findAll('div', attrs = {'class':'text_component ckOutput'})
    para = []

    for i in text_component:
        para.append(i.text)

    folder = "".join(x for x in link.split('/')[4] if x.isalnum()) 
    try: os.mkdir(f'Scrapped/{folder}')
    except: pass

    text = f'''
    <h1> {title} </h1>

    {[f'<p>{i}</p><br>' for i in para]}
    '''

    with open(f'Scrapped/{folder}/{sno}-{title}.html', 'w', encoding="utf-8") as f:
        f.write(text)


for i in Carousel_item__UUZAx:
    for j in i.findAll('a'):

        link = j['href']
        req = requests.get(link)
        soup = bs(req.content, 'html5lib')

        session = soup.findAll('div', attrs = {'class':'session'})
        for c, k in enumerate(session):
            link = k.a['href']
            print(link)
            print()

            try: save_scrapped(link, c+1)
            except: pass
