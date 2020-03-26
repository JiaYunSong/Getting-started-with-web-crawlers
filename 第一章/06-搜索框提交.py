import requests
kv = {'wd':'Python'}
r = requests.get('http://www.baidu.com/s', params=kv)
print(r.request.url)
print(r.text)
