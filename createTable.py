import pymysql

def create_table():
    config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'root',
        'db':'56network',
        'charset':'utf8mb4',
    }
    db = pymysql.connect(**config)
    sql = '''create table if not exists spider(
    title varchar(255) NOT NULL,
    url varchar(255),
    PRIMARY KEY (title)
    )'''
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('success')
    except:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    create_table()
