# from index import *

import requests
from bs4 import BeautifulSoup as bs
number = input('Enter Number')
url = f"https://www.gsmarena.com/samsung-phones-f-9-0-p{number}.php"
r = requests.get(url)
html = bs(r.text,'html.parser')
divPhone = html.find('div',{'class':'makers'})

linkPhone = divPhone.find_all('a')
# margedLink = linkPhone.__getattribute__('href')
# for link in linkPhone.__getitem__(0):
    # print(link) 
# test = linkPhone.get('href')

for link in linkPhone:
    modifiedLink = link.get('href')
    # print(test)
    print(f"https://www.gsmarena.com/{modifiedLink}")
    with open('pLink.txt','a') as out:
        out.writelines(f"https://www.gsmarena.com/{modifiedLink}\n")