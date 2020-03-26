# 网络爬虫入门

------------------------------

[TOC]

## Requests库

### 示例方法

```python
import requests
r = requests.get('https://www.icourse163.org/')
print(r.status_code)
r.encoding = 'utf-8'
print(r.text)
```

### 主要库函数

| 方法               | 说明                                    |
| ------------------ | --------------------------------------- |
| requests.request() | 构造一个请求，支撑以下各方法的基础方法  |
| request.get()      | 获取HTML网页的主要方法，对应于HTTP的GET |
| request.head()     | 对应于HTTP的GET                         |
| request.post()     | 对应于HTTP的POST                        |
| request.put()      | 对应于HTTP的PUT                         |
| request.patch()    | 对应于HTTP的PATCH                       |
| request.delete()   | 对应于HTTP的DELETE                      |

> #### request.get(url, params=None, **kwargs)
>
> - url：链接
> - params：url的额外参数
> - **kwargs：12个控制访问参数

### response对象

#### 示例

> ```python
> import requests
> r = requests.get('https://www.icourse163.org/')
> print(type(r))
> print(r.headers)
> ```
>
> 输出：
>
> ```python
> <class 'requests.models.Response'>
> {'Server': 'nginx', 'Date': 'Thu, 03 Oct 2019 16:05:45 GMT', 'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Server-Host': 'hzabj-mooc-online30', 'Set-Cookie': 'NTESSTUDYSI=0ede8b7bc14e4251abc3bedf8895381b; Domain=icourse163.org; Path=/, EDUWEBDEVICE=19a2df37bd424ecd8b67cc01fe3ec9ca; Domain=icourse163.org; Expires=Tue, 01-Oct-2024 16:05:45 GMT; Path=/', 'X-Application-Context': 'mooc:online:18382', 'Cache-Control': 'no-cache, must-revalidate', 'Expires': 'Sat, 20 Jul 2010 11:11:11 GMT', 'Pragma': 'no-cache', 'Content-Security-Policy': 'upgrade-insecure-requests', 'Content-Language': 'en-US', 'Content-Encoding': 'gzip'}
> ```

### 主要属性

| 属性                | 说明                                             |
| ------------------- | ------------------------------------------------ |
| r.status_code       | HTTP请求的返回状态，200表示连接成功，404表示失败 |
| r.text              | HTTP响应内容的字符串形式，即，url对应的网络内容  |
| r.encoding          | 从HTTP header中猜测的响应内容编码方式            |
| r.apparent_encoding | 从内容分析出的响应内容编码方式                   |
| r.content           | HTTP响应内容的二进制形式                         |

#### 示例

> ```python
> import requests
> r = requests.get('https://www.baidu.com/')
> print(r.encoding)
> print(r.text[1031:1100])
> 
> print(r.apparent_encoding)
> r.encoding = r.apparent_encoding
> print(r.text[1013:1080])
> ```
>
> 输出：
>
> ```html
> ISO-8859-1
> <input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn" autofocus>
> utf-8
> <input type=submit id=su value=百度一下 class="bg s_btn" autofocus>
> ```

### 异常

![01](\资源\01.JPG)

### 通用代码爬取框架

```python
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))
```



## HTTP协议常识

### 对资源的操作

![02](\资源\02.JPG)

> * put：更新时必须将所有字段重新提交
> * patch：局部更新字段，节省带宽

### requests库方法使用：

* head：

  * ```python
    r = requests.head(url)
    # r.headers = {'':''.......}
    # r.text = ''(空)
    ```

* post：

  * ```python
    payload = {'key1':'value1', 'key2':'value2'}
    r.requests.post(url, data = payload) # payload提交为form
    r.requests.post(url, data = 'ABC')   # 'ABC'提交为'data'
    ```

* put：

  * ```python
    payload = {'key1':'value1', 'key2':'value2'}
    r.requests.put(url, data = payload) # payload提交为form
    r.requests.put(url, data = 'ABC')   # 'ABC'提交为'data'
    ```



## requests.request方法

### 形式

```python
requests.request(method, url, **kwargs)
		--method:可以是'GET'/'HEAD'/'POST'/'PUT'/'PATCH'/'delete'/'OPTIONS'
```

### **kwargs

> * params:
>
>   * ```python
>    payload = {'key1':'value1', 'key2':'value2'}
>    r = requests.request('GET', url, params=payload)
>    ```
>  # url?key1=value1&key2=value2
>  ```
> 
> * data:
> 
>   * ```python
>  payload = {'key1':'value1', 'key2':'value2'}
>  r = requests.request('POST', url, data=payload)
>  # 或
>  r = requests.request('POST', url, data='主体内容')
>  ```
>
> * json:
>
>   * ```python
>    payload = {'key1':'value1'}
>    r = requests.request('POST', url, json=payload)
>    ```
>  ```
> 
> * headers:
> 
>   * ```python
>  payload = {'user-agent':'Chrome/10'}
>  r = requests.request('POST', url, headers=payload)
>  ```
>
> * cookies：字典或CookieJar
>
> * auth：元组，支持认证功能
>
> * files：字典类型，传输文件
>
>   * ```python
>    fs = {'file':open('data.xls', 'rb')}
>    r = requests.request('POST', url, files=payload)
>    ```
>  ```
> 
> * timeout：设定的超时时间，秒为单位，float
> 
> * proxies：字典类型，设定访问代理服务器，可以增加登录认证
> 
>   * ```python
>  pxs = {'http':'http://user:pass@10.10.10.1.1234',
>         'https':'https://10.10.10.1.4321'}
>  r = requests.request('GET', 'http://www.baaidu.com', proxies=pxs)
>  ```
>
> * allow_redirects:True/False，默认为True，重定向开关
>
> * stream:True/False，默认为True，获取内容立即下载开关
>
> * verify：True/False，默认为True，认证SSL证书开关
>
> * cert：本地SSL证书路径



## 网络爬虫简介

### 尺寸

![03](\资源\03.JPG)

### 负面影响

> 1. "骚扰"，为服务器带来巨大资源开销
> 2. 法律风险：版权问题，牟利风险
> 3. 隐私泄露问题

### 网络爬虫限制

> 1. 来源审查：检查User-Agent限制
> 2. Robots协议：告诉爬虫爬取策略，要求爬虫遵守
>
> > 会在网站根目录有Robots.txt，形式如下：
> >
> > > * \# 注释、\*代表所有、/代表根目录
> > > * User-agent: *
> > > * Disallow: /
> >
> > ![04](\资源\04.JPG)

## 模拟浏览器

> ```python
> import requests
> url = 'http://www.baidu.com'
> r = requests.get(url, timeout=30)
> print(r.request.headers)
> kv = {'user-agent':'Mozilla/5.0'}
> r = requests.get(url, headers=kv, timeout=30)
> print(r.request.headers)
> ```
>
> 输出：
>
> ```python
> {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 
> {'user-agent': 'Mozilla/5.0', 'Accept-Encoding':
> ```
>
> 其中第一个User-Agent给的是python-requests/2.22.0

## 填入搜索框

> 例如百度的：
>
> ```html
> http://www.baidu.com/s?wd=keyword
> ```
>
> 代码：
>
> ```python
> import requests
> kv = {'wd':'Python'}
> r = requests.get('http://www.baidu.com/s', params=kv)
> print(r.request.url)
> ```
>
> 输出：
>
> ```
> http://www.baidu.com/s?wd=Python
> ```

