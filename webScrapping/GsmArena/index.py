import numbers
import requests
from bs4 import BeautifulSoup as bs
number = input('Enter Number')
url = f"https://www.gsmarena.com/samsung-phones-f-9-0-p{number}.php"
r = requests.get(url)
html = bs(r.text,'html.parser')
# eTitle = html.find_all('div', {"class" : "job_seen_beacon"})
# for tag in eTitle:
#     title = tag.find_all('h2')
#     for loc in title:
#         print(loc.text)


# jobD = html.find_all('div', {"class" : "jobsearch-jobDescriptionText"})
# for p in jobD:
#     # des = p.find_all(p.text)
#     print(p)

# print(jobD)

divPhone = html.find('div',{'class':'makers'})
# titlePhone= divPhone[0].findAll('span').text

# print(type(divPhone))

# title = divPhone.find_all('span')

# for titlePhone in divPhone:
#     titlePhone.findAll('span')
#     print(titlePhone)

spanPhone = divPhone.find_all('span')
for titlePhone in spanPhone:
    # print(titlePhone.text)
    with open('pt.txt','a') as out:
        out.writelines(f"{titlePhone.text}\n")

# with open('pt.text','w') as out:
#     out.writelines(titlePhone.text)
# tileOfThePhone = open('phoneTitle.txt', 'w')
# tileOfThePhone.write(titlePhone.text)
# tileOfThePhone.close