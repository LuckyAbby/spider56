import requests
import bs4
import pymysql

root_url = 'http://www.56wangpan.com/'
url_info_list = []


def get_content():
    res = requests.get(root_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    url_list = soup.find_all('div', class_='info')
    for item in url_list:
        if item.find('div', class_='title'):
            title = item.a.attrs.get('title')
        if item.find('div', class_='address'):
            url = item.find('div', class_='address').string
        insert_table(title, url)

def insert_table(title, url):
    config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'root',
        'db':'56network',
        'charset':'utf8mb4',
    }
    db = pymysql.connect(**config)
    query_sql = 'select * from spider where title = %s'
    insert_sql = 'insert into spider(title, url) values(%s, %s)'
    cursor = db.cursor()
    try:
        query_value = (title)
        cursor.execute(query_sql, query_value)
        results = cursor.fetchall()
        if len(results) == 0:
            insert_value = (title, url)
            cursor.execute(insert_sql, insert_value)
            db.commit()
            print('--------------《%s》 insert table success-------------' % title)
            return True
        else:
            print('--------------《%s》 已经存在-------------' % title)
            return False
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    get_content()
