import requests
import random
from bs4 import BeautifulSoup

url = 'http://m.ip138.com/ip.asp'
kv = {'user-agent': 'Mozilla/5.0'}
for num in range(50):
    pa = {'ip': str(random.randint(0, 255))+'.'
                +str(random.randint(0, 255))+'.'
                +str(random.randint(0, 255))+'.'
                +str(random.randint(0, 255))}
    html = requests.get(url, params=pa, headers=kv, timeout=30)
    html.encoding = html.apparent_encoding
    mes = BeautifulSoup(html.text, 'html.parser')
    ele = mes.find('div', class_='module')
    print('\n'+pa['ip'])
    for ele2 in ele.find_all('p', class_='result'):
        print(ele2.text)
