
import requests, os
from bs4 import BeautifulSoup
import pandas as pd

try: os.mkdir('Scrapped')
except: pass

def fetch(turtle = '', tag='h3', attrs_class='family-name'):
    link = f'https://www.scrapethissite.com/pages/frames/?frame=i&family={turtle}'

    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html5lib')

    table = soup.findAll(tag, attrs = {'class': attrs_class})
    return table

data = {}
for j, i in enumerate(fetch()):
    lst = []
    turtle = i.text.strip()

    div = fetch(turtle, tag='div', 
        attrs_class='col-md-6 col-md-offset-3 turtle-family-detail'
    )[0]

    img = div.img
    h3 = div.h3
    p = div.p

    lst.append(img['src'].strip())
    lst.append(h3.text.strip())
    lst.append(p.text.strip())
    data.update({j : lst})

df = pd.DataFrame.from_dict(
    data, 
    orient='index'
)

df.to_csv(
    'Scrapped/Frames & iFrames.csv', 
    index = False, 
    header=False,
    encoding='utf-8'
)
