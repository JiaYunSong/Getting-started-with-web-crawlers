import requests
r = requests.get('https://www.icourse163.org/')
print(type(r))
print(r.headers)