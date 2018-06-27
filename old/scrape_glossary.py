from bs4 import BeautifulSoup
import requests

# create a beautiful soup object from web page
# get source code from website with requests
source = requests.get('https://docs.python.org/3/glossary.html').text

soup = BeautifulSoup(source, 'lxml')

for dt_tag in soup.find_all('dt'):
    print(dt_tag.text, dt_tag.next_sibling)

for dd_tag in soup.find_all('dd'):
    print(dd_tag.text, dd_tag.next_sibling)

# for dl in soup.find_all('dl', class_="glossary docutils"):
#     print(dl.dd)
