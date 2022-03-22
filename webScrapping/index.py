import requests
from bs4 import BeautifulSoup as bs

url = 'https://latestjobcircular.com/dhaka-thai-ltd-job-circular-november-2021/'
r = requests.get(url)
html = bs(r.text,'html.parser')
eTitle = html.find('title')

print(eTitle)
