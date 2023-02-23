# -*- coding: utf-8 -*-
import requests
import re
from oil_price.mysql_common import Mysql
from oil_price.table_name import table_name


class PushOilDataToMysql:
    def __init__(self):
        self.html = self.get_html_text()
        self.oil_data = self.parse_data()
        self.name = table_name()
        self.do_mysql = Mysql('localhost', 3306, 'root', 'zh850113', 'michael_oil_price')

    @staticmethod
    def get_html_text():
        url = 'http://youjia.chemcp.com/'
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""

    def parse_data(self):
        oil_data = []
        try:
            # 获取<table开头到</table>结尾的数据
            # 匹配规则, re.S 是因为“.”的作用是匹配除“\n”以外的任何字符, 而在html中有很多"\n"
            rule_table = '<table width="100%" border="0" cellpadding="4" cellspacing="1" bgcolor="#B6CCE4">\r\n(.*?)</table>'
            html_data = re.findall(rule_table, self.html, re.S)

            # 获取<tr>开头到</tr>结尾的数据，所有城市的内容
            # 匹配规则
            rule_tr = '<tr>\r\n(.*?)</tr>'
            citys_data = re.findall(rule_tr, html_data[0], re.S)  # data_list 为匹配的城市数据

            for i in range(1, len(citys_data)):
                city_data = citys_data[i]
                # 匹配规则
                rule_city_detail = '<td bgcolor="#FFFFFF">(.*?)</td>'
                city_detail_data = re.findall(rule_city_detail, city_data, re.S)
                area = city_detail_data[0].split('>')[1].split("<")[0]
                oil89 = eval(city_detail_data[1])
                oil92 = eval(city_detail_data[2])
                oil95 = eval(city_detail_data[3])
                oil98 = eval(city_detail_data[4])
                oil0 = eval(city_detail_data[5])
                update_time = city_detail_data[6]
                oil_data.append((area, oil89, oil92, oil95, oil98, oil0, update_time))
        except:
            print("获取油价数据失败")
        return oil_data

    def create(self):
        sql_create_table = 'create table `%s`(id int auto_increment,`area` varchar(20),`oil89` varchar(20),`oil92` varchar(20),`oil95` varchar(20),`oil98` varchar(20), `oil0` varchar(20), `update_time` varchar(255), primary key(id))' % self.name
        self.do_mysql.execute(sql_create_table)

    def insert(self):
        for i in range(len(self.oil_data)):
            sql_insert = 'insert into %s(area, oil89, oil92, oil95, oil98, oil0, update_time) value%s' % (self.name, self.oil_data[i])
            self.do_mysql.execute(sql_insert)


if __name__ == '__main__':
    test = PushOilDataToMysql()
    test.create()
    test.insert()