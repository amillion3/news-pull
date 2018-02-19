import newspaper

cnn_paper = newspaper.build('http://cnn.com')

for article in cnn_paper.articles:
  print(article.url)

for category in cnn_paper.category_urls():
    print(category)

article = cnn_paper.articles[0]

article.download()

article.html

article.parse()

article.authors

article.text

article.top_image