from urllib import request
from bs4 import BeautifulSoup
import re
response = request.urlopen('https://www.cnki.net')
html = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
print(html.find_all(re.compile("a*")))

input('\n-----------------------------\n任意键结束...')
