from bs4 import BeautifulSoup
import requests


def anki(keyword, word_type):
    if word_type.lower() == verb:
        url = f'https://www.verbformen.com/conjugation/?w={keyword}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        #to do create loop to get table from 7-9
        verb = soup.find_all('table')[3]


def text_strip(verb):
    column_data = verb.find_all('tr')
    for row in column_data:
        row_data = row.find_all('td')
        ind_row = [data.text.strip() for data in row_data]
        print(ind_row)






