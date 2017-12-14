import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = ('utr-8')
        return r.text
    except:
        print('获取页面数据失败')
        return 'error'

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    divList = soup.find_all('div', class_="rank-list")
    contents = []
    for div in divList:
        typeName = div.find('h3', class_="wrap-title lang").contents[0]
        with open('hongxiutianxiang.txt', 'a+') as f:
            f.write("\n小说种类：{} \n".format(typeName))
        divContainer = div.find('div', class_="book-list")
        liList = divContainer.find_all('li')
        for li in liList:
            content = {}
            if li.get('class') and li['class'].index('unfold') != -1:
                content['name'] = li.find('a')['title']
                content['link'] = 'https://www.hongxiu.com' + li.find('a')['href']
            else:
                divName = li.find('div', class_="name-box")
                content['name'] = divName.a['title']
                content['link'] = 'https://www.hongxiu.com' + divName.a['href']
            contents.append(content)
            with open('hongxiutianxiang.txt', 'a') as f:
                f.write("小说名：{:<} \t 小说地址：{:<} \n".format(content['name'], content['link']))

url = 'https://www.hongxiu.com/'
get_content(url)
