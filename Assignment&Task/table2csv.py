
import requests, os
import pandas as pd
from bs4 import BeautifulSoup

try: os.mkdir('output')
except: pass

link = 'https://www.ridgid.com/in/en/700-power-drive'

req = requests.get(link)
soup = BeautifulSoup(req.content, 'html5lib')

table = soup.findAll('table', 
    attrs = {
        'class':'table-overflow productTable'
    }
)

for ind, tab in enumerate(table):
    tr = tab.findAll('tr')
    row_list = {}
    counter = 0

    for row in tr:
        co_list = []

        for i in row:
            co_list.append(i.text.strip())

        co_list = [x for x in co_list if x not in ['']]
        if ind != 2: # this condition is to handle nested row for (WEIGHT LB KG)
            
            if counter == 0:
                length = len(co_list)

            if counter == 1:
                for _ in range(length):
                    co_list.append('')

                co_list.pop()
                co_list = co_list[::-1]

        row_list.update({counter : co_list})
        counter += 1

    df = pd.DataFrame.from_dict(row_list, orient='index')
    df.to_csv(f'output/table_{ind}.csv', header=False, index=False)
