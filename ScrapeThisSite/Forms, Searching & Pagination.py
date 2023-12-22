
import requests, os
from bs4 import BeautifulSoup as bs
import pandas as pd

try: os.mkdir('Scrapped')
except: pass

link = 'https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=25'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

data = {}
table = soup.findAll('table', attrs = {'class':'table'})[0]
tr = table.findAll('tr')

for i, j in enumerate(tr):
    lst = []
    if i == 0:
        th = j.findAll('th')
        for m in th:
            lst.append(m.text.strip())
    else:
        td = j.findAll('td')
        for n in td:
            lst.append(n.text.strip())
    data.update({i : lst})

df = pd.DataFrame.from_dict(
    data, 
    orient='index'
)

df.to_csv(
    'Scrapped/Forms, Searching & Pagination.csv', 
    index = False, 
    encoding='utf-8'
)
