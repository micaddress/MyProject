# encoding='utf-8'
# -*- coding: utf-8 -*-
from pymysql import *
import pymysql

class Mysql:
    def __init__(self, host, port, user, password, db, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    def connectsql(self):
        self.conn = connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            passwd=self.password,
                            db=self.db,
                            charset=self.charset)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def closesql(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        try:
            self.connectsql()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
            self.conn.commit()

            self.closesql()

        except Exception as e:
            print(e)




