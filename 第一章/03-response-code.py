import requests
r = requests.get('https://www.baidu.com/')
print(r.encoding)
print(r.text[1031:1100])

print(r.apparent_encoding)
r.encoding = r.apparent_encoding
print(r.text[1013:1080])
