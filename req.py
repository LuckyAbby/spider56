import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.baidu.com")
bs = BeautifulSoup(r.text, 'lxml')
print(bs.title)
print(bs.title.name)
print(bs.find_all('input'))
for item in bs.find_all('input'):
    print(item.get('value'))

print(bs.head.contents)
print(bs.prettify())
for item in bs.head.descendants:
    print(item)
print(bs)
print(bs.find('a').string)
print(r.headers)
print(r.apparent_encoding)
