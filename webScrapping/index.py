import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.indeed.com/jobs?q=python&l=Usk%2C%20WA&vjk=26dd1928feab499f'
r = requests.get(url)
html = bs(r.text,'html.parser')
eTitle = html.find_all('div', {"class" : "job_seen_beacon"})
for tag in eTitle:
    title = tag.find_all('h2')
    for loc in title:
        print(loc.text)
