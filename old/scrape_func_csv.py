from bs4 import BeautifulSoup
import requests
import csv
import json

# create a beautiful soup object from web page
# get source code from website with requests
source = requests.get('https://docs.python.org/3/library/functions.html').text

soup = BeautifulSoup(source, 'lxml')

# set up csv file to accept data under headings of... 'head', 'row'
# This method also extracts some no utf-8 symbols
# eg super([type[, object-or-type]])Â¶ encoding="latin-1"
# encoding removes the Â but not ¶
csv_file = open('scrape_func.csv', 'w', encoding="latin-1")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['head', 'summary'])

# This method also extracts some no utf-8 symbols
# eg super([type[, object-or-type]])Â¶
# will remove them after parsing
for dl_tag in soup.find_all('dl', class_="function"):

    head = dl_tag.dt.text
    print(head)

    summary = dl_tag.dd.text
    print(summary)

    csv_writer.writerow([head, summary])

# close csv file
csv_file.close()

# remove no utf-8... need to strip() the chars maybe??
"""
with open(csv_file, "r") as fp:
    for line in fp:
        line = line.strip()
        line = line.decode('utf-8', 'ignore').encode("utf-8")
"""

data = head, summary
saved_data = json.dumps(data)
print(saved_data)
