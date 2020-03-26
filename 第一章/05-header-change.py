import requests

url = 'https://www.amazon.cn/'
r = requests.get(url, timeout=30)
print(r.request.headers)

kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=kv, timeout=30)
print(r.request.headers)
