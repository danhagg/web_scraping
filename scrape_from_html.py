from bs4 import BeautifulSoup
import requests

# create a beautiful soup object from file
# soup object of parsed html
with open('example.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# can print out normal or pretty(indents)
print(soup.prettify())

# match_title = soup.title.text

# needs underscore as class is reserved word in python
match_class = soup.find('div', class_='footer')

match_id = soup.find('div', id='footer')

print(match)

# if we have an article div with multiple sub elements
article = soup.find('div', id='article')

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

# Use find_all to get all text from a given tag
for article in soup.find_all('div', id='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    # blank line between arti
    print()
