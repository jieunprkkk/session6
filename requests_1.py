from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from openpyxl import Workbook

url='https://quotes.toscrape.com/'

wb = Workbook()
ws = wb.active
ws.append(['넘버', '어록', '위인'])
    
response = requests.get(url)
    
if response.status_code == 200:
    html_text = response.text
    soup = bs(html_text, 'html.parser')
    
    quotes = soup.select('body > div > div:nth-child(2) > div.col-md-8 > div > span:first-child')
    author = soup.select('body > div > div:nth-child(2) > div.col-md-8 > div > span:nth-child(2) > small')
    
    quotes = list(map(lambda x: x.text.strip(), quotes))
    author = list(map(lambda x: x.strip(), quotes))
    for i, (quotes, author) in enumerate(zip(quotes, author), start = 1):
        ws.append([i, quotes, author])
    filename = '어록 모음집.xlsx'
    wb.save(filename)
    
else:
    print("요청 실패, 상태 코드")