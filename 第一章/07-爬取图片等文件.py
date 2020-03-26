import requests
import os
url = "http://www.caux.cn/static/images/header-logo.png"
root = 'E:/1.课内资料/2-大二上课程/自-Python爬虫/MOOC/第一章/资源/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')