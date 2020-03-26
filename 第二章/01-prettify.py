from urllib import request
from bs4 import BeautifulSoup
response = request.urlopen('https://www.cnki.net')
html = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
print(html.prettify())