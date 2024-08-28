from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapping regionu a kapacit detskych skupinek  
# následné vytvoření DF k importu pro analýzu

url_DS = 'https://evidence.mpsv.cz/eEDS/index.php?list'
session = HTMLSession()
response = session.get(url_DS)
soup = BeautifulSoup(response.text, 'html.parser') 
table = soup.find('div', {'class':'innerContentDiv'})

regions =[]
if table:
    # find all the rows of regions names in the "table" body
    names = table.find_all('b')
    for reg in names:
        reg = reg.text.strip()
        regions.append(reg)
# print(DS_columns_data)

capacity_after_br = []
if table:
    capacity = table.find_all('br')
    for br in capacity:
        ns = br.next_sibling
        if ns and isinstance(ns, str):
            text = ns.strip()
            # regex
            match = re.search(r'celková kapacita:\s*([\d\s]+)\s*míst', text)
            if match:
                # extract the number 
                capacity_number = match.group(1).replace(' ', '')
                capacity_after_br.append(capacity_number)

i = {'Kapacita': capacity_after_br,
     'Kraj': regions}

DS_tabulka = pd.DataFrame(i)
DS_tabulka.insert(loc=0, column='ZarizeniTyp', value='Dětská skupinka')
# print(DS_tabulka)
