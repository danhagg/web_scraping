from bs4 import BeautifulSoup
import requests
import json

# create a beautiful soup object from web page
# get source code from website with requests
source = requests.get('https://docs.python.org/3/library/functions.html').text

soup = BeautifulSoup(source, 'lxml')

# This method also extracts some no utf-8 symbols
# eg super([type[, object-or-type]])Â¶
# will remove them after parsing
data = {}
for dl_tag in soup.find_all('dl', class_="function"):

    head = dl_tag.dt.text
    print(head)

    summary = dl_tag.dd.text
    print(summary)

    data.update({head: summary})

# remove no utf-8... need to strip() the chars maybe??
"""
with open(csv_file, "r") as fp:
    for line in fp:
        line = line.strip()
        line = line.decode('utf-8', 'ignore').encode("utf-8")
"""

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print(type(data))
