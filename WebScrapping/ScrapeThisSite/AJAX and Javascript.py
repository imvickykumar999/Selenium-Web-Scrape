
import requests
import pandas as pd

writer = pd.ExcelWriter(
    'Scrapped/AJAX and Javascript.xlsx', 
    engine='xlsxwriter'
)

for i in range(2010, 2016):
    ajax = f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={i}'
    r = requests.get(ajax)
    data = r.json()

    for j in data: 
        j.pop('year')

        try: j['Best Picture'] = j.pop('best_picture')
        except: j['Best Picture'] = False
        
        j['Title'] = j.pop('title')
        j['Awards'] = j.pop('awards')
        j['Nominations'] = j.pop('nominations')

    df = pd.DataFrame(data)
    pd.DataFrame(df).to_excel(writer, 
        sheet_name = f'Sheet_{i}', 
        index = False, 
        header=True
    )

writer.save()
