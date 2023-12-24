
import requests, os
from bs4 import BeautifulSoup as bs
import pandas as pd

try: os.mkdir('Scrapped')
except: pass

writer = pd.ExcelWriter(
    'Scrapped/Forms, Searching & Pagination.xlsx', 
    engine='xlsxwriter'
)

for page in range(1, 25):
    link = f'https://www.scrapethissite.com/pages/forms/?page_num={page}&per_page=25'
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

    pd.DataFrame(df).to_excel(writer, 
        sheet_name = f'Sheet_{page}', 
        index = False, 
        header=False
    )

writer.save()
