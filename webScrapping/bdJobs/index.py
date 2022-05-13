import requests
from bs4 import BeautifulSoup as bs

url = "https://jobs.bdjobs.com/jobsearch.asp?fcatId=4&icatId="
r = requests.get(url)
html = bs(r.text,'html.parser')
print(html.text)