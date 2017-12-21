import requests
import bs4
import pymysql

root_url = 'http://www.56wangpan.com/'
url_info_list = []

def get_urls():
    res = requests.get(root_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    url_list = soup.find_all('div', class_='info')
    print(url_list)
    for item in url_list:
        if item.find('div', class_='title'):
            title = item.a.attrs.get('title')
        if item.find('div', class_='address'):
            url = item.find('div', class_='address').string
        url_info_list.append({
        'title':title, 'url':url
        })
    return url_info_list
print(get_urls())
