import requests


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        print(r.request.headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'http://now.data.itxdl.cn/xiaoquxinwen/2019/0513/4929.html?utm_source=bdwk'
    print(getHTMLText(url))
