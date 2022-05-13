import requests
from bs4 import BeautifulSoup as bs
url = "https://jobs.bdjobs.com/jobsearch.asp?log=stats"
r = requests.get(url)
html = bs(r.text,'html.parser')
jobTitle = html.find_all('div', {"class" : "job-title-text"})
print(len(jobTitle))
for title in jobTitle:

    print(title.text)