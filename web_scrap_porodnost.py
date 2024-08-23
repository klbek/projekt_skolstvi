from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

def extract_first_two_columns(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the table by its ID
    table = soup.find('table', {'id': 'tabData'})
    
    # Extract the first two columns data
    first_two_columns_data = []
    if table:
        # Find all the rows in the table body
        rows = table.find_all('tr')
        for row in rows:
            # Find the first two 'td' elements in each row
            columns = row.find_all('td', limit=2)
            if len(columns) >= 2:
                # Extract the text from the first and second columns and clean it up
                first_column_text = columns[0].get_text(strip=True)
                second_column_text = columns[1].get_text(strip=True).replace("\xa0", "")
                first_two_columns_data.append((first_column_text, second_column_text))
            elif len(columns) == 1:
                # If there is only one column, add the second column as an empty string
                first_column_text = columns[0].get_text(strip=True)
                first_two_columns_data.append((first_column_text, ''))
    
    return first_two_columns_data

def porodnost(url):
    session = HTMLSession()
    response = session.get(url)
    born = extract_first_two_columns(response.text)
    return pd.DataFrame(born, columns=["Kraj", "PocetNarozenychDeti"])

# návrh na upgrade - rok porodnosti by šel scrapovat extract_first_two_columns
porodnost2023 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&z=T&f=TABULKA&skupId=586&katalog=33155&pvo=DEM07&pvo=DEM07&evo=v1450_!_IK-CR-K_1&c=v3~8__RP2023#w=').assign(Rok = 2023)
porodnost2022 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=DEM07&z=T&f=TABULKA&skupId=586&katalog=33155&c=v3~8__RP2022&&evo=v1450_!_IK-CR-K_1&str=v741').assign(Rok = 2022)
porodnost2021 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=DEM07&z=T&f=TABULKA&skupId=586&katalog=33155&c=v3~8__RP2021&&evo=v1450_!_IK-CR-K_1&str=v741').assign(Rok = 2021)
porodnost2020 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=DEM07&z=T&f=TABULKA&skupId=586&katalog=33155&c=v3~8__RP2020&&evo=v1450_!_IK-CR-K_1&str=v741').assign(Rok = 2020)
porodnost2019 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=DEM07&z=T&f=TABULKA&skupId=586&katalog=33155&c=v3~8__RP2019&&evo=v1450_!_IK-CR-K_1&str=v741').assign(Rok = 2019)
porodnost2018 = porodnost('https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=DEM07&z=T&f=TABULKA&skupId=586&katalog=33155&c=v3~8__RP2018&&evo=v1450_!_IK-CR-K_1&str=v741').assign(Rok = 2018)

porodnostSeznam = [porodnost2023, porodnost2022, porodnost2021, porodnost2020, porodnost2019, porodnost2018] 
porodnost_tabulka = pd.concat(porodnostSeznam, ignore_index=True)
# print(porodnost_tabulka.head(20))
