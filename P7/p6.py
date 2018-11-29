import re
import requests

from bs4 import BeautifulSoup


def GetPageToSoup(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return BeautifulSoup(r.text, features="html.parser")


def liProcessing(li):
    return {'title': li.select('a > em')[0].text,
            'price': li.find(class_='p-price').i.text,
            'href': 'http:' + li.find(class_='p-name p-name-type-2').a['href']}


def Processing(url):
    soup = GetPageToSoup(url)
    return [liProcessing(i) for i in soup.find(id='J_goodsList').select('ul > li')]


ans = Processing('https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&suggest=1.def.0.V01&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=5de1e034dd4b4981a46121b0b803bb21')
# print(ans)
for i in ans:
    print(i)

#### python3 p6.py > output.md
## ans in "output.md"