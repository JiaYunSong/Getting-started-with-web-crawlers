import requests
r = requests.get('https://www.icourse163.org/')
print(r.status_code)
r.encoding = 'utf-8'
print(r.text)