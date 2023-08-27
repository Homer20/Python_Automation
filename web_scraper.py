import requests
from bs4 import BeautifulSoup

# Making a variable for the website url
url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'

# Sending an http get request to the url
response = requests.get(url)

# Extracting the html content of the url
html_content = response.content

# Parsing the html content and creating a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Search html elements in the content
article_content = soup.find('div', {'class': 'article__content'})

# Printing the content of the article
print('Content:', article_content.get_text(' ', strip=True))