import requests
import bs4

root_url = 'http://www.56wangpan.com/'
url_info_list = []

def get_urls():
    res = requests.get(root_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    url_list = soup.find_all('div', class_='info')
    # print(url_list)
    for item in url_list:
        # print(item)
        title = item.a.attrs.get('title')
        # .attrs.get('title')
        # print('title is', title)
        url = item.find('div', class_='address').string
        # url = item.
        # .string
        print('url is', url)
        # url_info_list.append({
        # 'title':title, 'url':url
        # })
    return url_info_list
print(get_urls())
