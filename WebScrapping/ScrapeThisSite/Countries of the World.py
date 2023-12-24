
import requests, os
from bs4 import BeautifulSoup as bs
import pandas as pd

try: os.mkdir('Scrapped')
except: pass

link = 'https://www.scrapethissite.com/pages/simple/'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

data = {}
countryname = []
countrycapital = []
countrypopulation = []
countryarea = []

country_name = soup.findAll('h3', attrs = {'class':'country-name'})
for i in country_name:
    countryname.append(i.text.strip())

country_capital = soup.findAll('span', attrs = {'class':'country-capital'})
for i in country_capital:
    countrycapital.append(i.text.strip())

country_population = soup.findAll('span', attrs = {'class':'country-population'})
for i in country_population:
    countrypopulation.append(i.text.strip())

country_area = soup.findAll('span', attrs = {'class':'country-area'})
for i in country_area:
    countryarea.append(i.text.strip())

data.update({"Country" : countryname})
data.update({"Capital" : countrycapital})
data.update({"Population" : countrypopulation})
data.update({"Area (km2)" : countryarea})

df = pd.DataFrame.from_dict(
    data, 
    orient='index'
)

df.transpose().to_csv(
    'Scrapped/Countries of the World.csv', 
    index = False, 
    encoding='utf-8'
)
