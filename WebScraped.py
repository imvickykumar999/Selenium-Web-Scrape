
import requests, os
from bs4 import BeautifulSoup as bs

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

    try: os.mkdir('Scrapped')
    except: pass

    try: os.mkdir(f'Scrapped/{folder}')
    except: pass

    text = f'''
    <h1> {title} </h1>

    <p> {[f'{i}<br><br>' for i in para]} </p>
    '''

    with open(f'Scrapped/{folder}/{title}.html', 'w', encoding="utf-8") as f:
        f.write(text)


link = 'https://www.upgrad.com/learn/'
req = requests.get(link)
soup = bs(req.content, 'html5lib')
Carousel_item__UUZAx = soup.findAll('div', attrs = {'class':'Carousel_item__UUZAx'})

for i in Carousel_item__UUZAx:
    for j in i.findAll('a'):

        link = j['href']
        req = requests.get(link)
        soup = bs(req.content, 'html5lib')

        session = soup.findAll('div', attrs = {'class':'session'})
        for k in session:
            link = k.a['href']
            print(link)
            print()

            try: save_scrapped(link)
            except: pass
