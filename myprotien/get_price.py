# -*- coding: UTF-8 -*-
import sys
sys.path.append('D:/workspace/MyProject/')
from myprotien import get_myprotien_DB
from lxml import etree
from ronglian_sms_sdk import SmsSDK
import requests
import datetime


def get_data_from_myprotien():
    creatien_url = 'https://www.myprotein.cn/sports-nutrition/creatine-monohydrate-powder/10530050.html'

    creatien_response = requests.get(creatien_url)
    creatien_tree = etree.HTML(creatien_response.text)

    creatien_name = creatien_tree.xpath('//title/text()')[0].replace("\t","").replace("\n","").replace(" ","").split('|')[0]
    print(creatien_name)

    c_weight = creatien_tree.xpath("//li[@class='athenaProductVariations_listItem']/button//text()")
    creatien_weight = ''
    for i in range(len(c_weight)):
        cw = c_weight[i].replace('\n', '').replace('\t', '').replace(' ','')
        creatien_weight += cw
    print(creatien_weight)

    creatien_price = creatien_tree.xpath("//div[@class='athenaProductPage_lastColumn']//div[@class='athenaProductPage_productPrice']//span[@class='productPrice_schema productPrice_priceAmount']/text()")[0]
    creatien_price = float(creatien_price)
    print(creatien_price)

    creatien_mark = creatien_tree.xpath("//div[@class='stripBanner']/a/text()")[0].replace("\t","").replace("\n","").replace(" ","")
    print(creatien_mark)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    protien_url = 'https://www.myprotein.cn/sports-nutrition/impact-whey-protein/10530943.html?variation=10530960'

    protien_response = requests.get(protien_url)
    protien_tree = etree.HTML(protien_response.text)

    protien_name = str(protien_tree.xpath("//div[@class='productName']/h1/text()")[0])
    print(protien_name)

    protien_weight = '5kg'

    protien_price = protien_tree.xpath("//div[@class='athenaProductPage_productPrice_top']//span[@class='productPrice_schema productPrice_priceAmount']/text()")[0]
    protien_price = float(protien_price)
    print(protien_price)

    protien_mark = protien_tree.xpath("//div[@class='stripBanner']/a/text()")[0].replace("\t","").replace("\n","").replace(" ","")
    print(protien_mark)

    recording_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    creatien_dict = {'creatien_name': creatien_name,
                     'creatien_weight': creatien_weight,
                     'creatien_price': creatien_price,
                     'creatien_mark': creatien_mark}
    protien_dict = {'protien_name': protien_name,
                    'protien_weight': protien_weight,
                    'protien_price': protien_price,
                    'protien_mark': protien_mark}
    check_data(creatien_dict, protien_dict, recording_time)


def check_data(creatien_dict, protien_dict, recording_time):
    creatien_name = creatien_dict['creatien_name']
    creatien_weight = creatien_dict['creatien_weight']
    creatien_new_price = creatien_dict['creatien_price']
    creatien_mark = creatien_dict['creatien_mark']

    protien_name = protien_dict['protien_name']
    protien_weight = protien_dict['protien_weight']
    protien_new_price = protien_dict['protien_price']
    protien_mark = protien_dict['protien_mark']
    connection = get_myprotien_DB.conn
    cursor = connection.cursor()

    sql_creatine_min_price = """select min(price) from myprotien_price where name like '%肌酸%'"""
    sql_protien_min_price = """select min(price) from myprotien_price where name like '%蛋白%'"""
    cursor.execute(sql_creatine_min_price)
    return_flag = cursor.fetchone()[0]
    creatien_last_price = protien_last_price = ''
    if return_flag is not None:
        creatien_min_price = float(return_flag)
        cursor.execute(sql_protien_min_price)
        protien_min_price = float(cursor.fetchone()[0])

        sql_creatine_max_price = """select max(price) from myprotien_price where name like '%肌酸%'"""
        sql_protien_max_price = """select max(price) from myprotien_price where name like '%蛋白%'"""
        cursor.execute(sql_creatine_max_price)
        creatien_max_price = float(cursor.fetchone()[0])
        cursor.execute(sql_protien_max_price)
        protien_max_price = float(cursor.fetchone()[0])

        sql_creatine_last_price = """select price from myprotien_price where id = (select max(id) from myprotien_price where name like '%肌酸%')"""
        sql_protien_last_price = """select price from myprotien_price where id = (select max(id) from myprotien_price where name like '%蛋白%')"""
        cursor.execute(sql_creatine_last_price)
        creatien_last_price = float(cursor.fetchone()[0])
        cursor.execute(sql_protien_last_price)
        protien_last_price = float(cursor.fetchone()[0])

    sql_to_myprotien_price = '''insert into myprotien_price(
                                                            record_time,
                                                            name,
                                                            weight,
                                                            price,     
                                                            mark
                                                            ) values (%s,%s,%s,%s,%s)'''

    if creatien_new_price != creatien_last_price or return_flag is None:
        cursor.execute(sql_to_myprotien_price,(recording_time,
                                               creatien_name,
                                               creatien_weight,
                                               creatien_new_price,
                                               creatien_mark))

    if protien_new_price != protien_last_price or return_flag is None:
        cursor.execute(sql_to_myprotien_price,(recording_time,
                                               protien_name,
                                               protien_weight,
                                               protien_new_price,
                                               protien_mark))
    connection.commit()
    cursor.close()
    connection.close()

    if creatien_last_price != '':
        if creatien_new_price != creatien_last_price or protien_new_price != protien_last_price:
            creatine_str = '肌酸价格没变'
            protien_str = '蛋白粉价格没变'
            if creatien_new_price < creatien_last_price:
                creatine_str = 'myprotien 1公斤肌酸已经降价,当前价格 ' + str(creatien_new_price) + ' 比上次价格 ' + str(creatien_last_price) + ' 降了 ' + str(creatien_last_price - creatien_new_price) + '元' + ',之前最低价 ' + str(creatien_min_price) + ' 最高价 ' + str(creatien_max_price)
            elif creatien_new_price > creatien_last_price:
                creatine_str = 'myprotien 1公斤肌酸已经涨价了,当前价格 ' + str(creatien_new_price) + '比上次价格 ' + str(creatien_last_price) + ' 涨了 ' + str(creatien_new_price - creatien_last_price) + '元' + ',之前最低价 ' + str(creatien_min_price) + ' 最高价 ' + str(creatien_max_price)

            if protien_new_price < protien_last_price:
                protien_str = 'myprotien 5公斤蛋白粉已经降价,当前价格 ' + str(protien_new_price) + ' 比上次价格 ' + str(protien_last_price) + ' 降了 ' + str(protien_last_price - protien_new_price) + '元' + ',之前最低价 ' + str(protien_min_price) + ' 最高价 ' + str(protien_max_price)
            elif protien_new_price > protien_last_price:
                protien_str = 'myprotien 5公斤蛋白粉已经涨价了,当前价格 ' + str(protien_new_price) + ' 比上次价格 ' + str(protien_last_price) + ' 涨了 ' + str(protien_new_price - protien_last_price) + '元' + ',之前最低价 ' + str(protien_min_price) + ' 最高价 ' + str(protien_max_price)

            send_message(creatine_str, protien_str)


def send_message(creatine_str, protien_str):
    accid = '8aaf07087f77bf96017faf9863d4176b'
    acc_token = 'a855521212a347118db04e2a6a8813cf'
    app_id = '8aaf07087f77bf96017faf9865031772'

    sdk = SmsSDK(accid, acc_token, app_id)
    tid = '1'
    mobile = '13339287298'
    datas = (creatine_str, protien_str)
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


if __name__ == '__main__':
    get_data_from_myprotien()
