# from index import *

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com/samsung-phones-9.php'
r = requests.get(url)
html = bs(r.text,'html.parser')
divPhone = html.find('div',{'class':'makers'})

linkPhone = divPhone.find_all('a')
# margedLink = linkPhone.__getattribute__('href')
for link in linkPhone.__getitem__(0):
    print(link) 
# test = linkPhone.get('href')

# print(f"https://www.gsmarena.com/{test}")