
import requests, os
from bs4 import BeautifulSoup
import pandas as pd

try: os.mkdir('Scrapped')
except: pass

writer = pd.ExcelWriter(
    'Scrapped/Frames & iFrames.xlsx', 
    engine='xlsxwriter'
)

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

    turtle_image = fetch(turtle, tag='img', attrs_class='turtle-image center-block')[0]
    family_name = fetch(turtle, tag='h3', attrs_class='family-name')[0]
    description = fetch(turtle, tag='p', attrs_class='lead')[0]

    lst.append(turtle_image['src'].strip())
    lst.append(family_name.text.strip())
    lst.append(description.text.strip())
    data.update({j : lst})

df = pd.DataFrame.from_dict(
    data, 
    orient='index'
)

pd.DataFrame(df).to_excel(writer, 
    sheet_name = 'turtle', 
    index = False, 
    header=False
)
writer.save()
