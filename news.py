from newspaper import Article

url = 'https://docs.python.org/3/library/functions.html'
article = Article(url)

article.download()

article.html

print(article.html)

article.parse()
a = article.parse()
print(type(a))
