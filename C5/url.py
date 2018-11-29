# urllib3 is a powerful, sanity-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too. urllib3 brings many critical features that are missing from the Python standard libraries:
#
# Thread safety.
# Connection pooling.
# Client-side SSL/TLS verification.
# File uploads with multipart encoding.
# Helpers for retrying requests and dealing with HTTP redirects.
# Support for gzip and deflate encoding.
# Proxy support for HTTP and SOCKS.
# 100% test coverage.
# urllib3 is powerful and easy to use:

# import urllib3
#
# http = urllib3.PoolManager()
# res = http.request("GET", r"https://list.jd.com/list.html?cat=670,671,672")
#
# print(res.status)
#
# print(res.data.decode('utf-8'))

import requests
from bs4 import BeautifulSoup

res = requests.get(r'https://list.jd.com/list.html?cat=670,671,672')
resText = res.text

# print(resText)

bs = BeautifulSoup(resText,'lxml')
bsList = bs.find_all('li',class_ = 'gl-item')

for item in bsList:
    print(item.find('div', class_='p-name').find('a'))