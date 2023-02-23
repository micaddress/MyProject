# encoding='utf-8'
import pymysql
params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'zh850113',
            'database': 'michael_user_info',
            'port': 3306,
            'charset': 'utf8mb4'
        }
conn = pymysql.connect(**params)
conn.autocommit(True)
cursor = conn.cursor()





