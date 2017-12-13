import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        print('get_html error')
        return "error"

def get_content(url):
    contents = []
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    liList = soup.find_all('li', class_=" j_thread_list clearfix")
    for item in liList:
        content = {}
        try:
            content['title'] = item.find('a', class_="j_th_tit").get('title')
            content['link'] = "http://tieba.baidu.com/" + item.find('a', class_="j_th_tit").get('href')
            content['name'] = item.find('span', attrs={'class': 'tb_icon_author '}).text.strip()
            contents.append(content)
        except:
            print('get list error')
            return 'error'
    return contents

def sava_file(contents):
    with open('PostBar.txt', 'a+') as f:
        for content in contents:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \n'.format(content['title'], content['link'], content['name']))
        print('all done')

def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url = base_url + '&pn=' + str(50 * i)
        url_list.append(url)
    print('all downloaded')

    for item in url_list:
        contents = get_content(item)
        sava_file(contents)
    print('all saved')

base_url = 'https://tieba.baidu.com/f?kw=%E5%8D%8E%E8%83%A5%E5%BC%95&ie=utf-8'
deep = 4
main(base_url, deep)
