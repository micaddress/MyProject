# -- coding: utf-8 --
import get_user_info_DB as userDB

def get_info_by_phone(phone):
    phone = "'" + str(phone) + "'"
    print(phone)
    # userDB.conn.commit()
    cursor = userDB.cursor
    sql_by_phone = "select * from custom where phone = " + phone
    print(sql_by_phone)
    cursor.execute(sql_by_phone)
    result = cursor.fetchone()
    print(result)
    if result:
        return_str = '客户名称: ' + str(result[1]) + '\n' + '号码 : ' + str(result[2]) + '\n' + '出生年月 : ' + str(result[3]) + \
                     '\n' + '年龄 : ' + str(result[4]) + '\n' + '第一次来店时间: ' + str(result[5]) + '\n' + '到店次数: ' + str(result[6]) + \
                     '次' + '\n' + '付款时间: ' + str(result[7]) + '\n' + '提车时间: ' + str(result[8]) + '\n' + '曾用车: ' + str(result[9]) + \
                     '\n' + '曾用车价格: ' + str(result[10]) + '\n' + '预购车型: ' + str(result[11]) + '\n' + '预购车型价格: ' + str(result[12]) + \
                     '\n' + '实提车型: ' + str(result[13]) + '\n' + '实提车价: ' + str(result[14]) + '\n' + '备注: ' + result[15]
    else:
        return_str = '未查询到此号码 (' + phone + ') 所绑定的客户信息'
    return return_str


def get_info_by_name(name):
    name = "'" + str(name) + "'"
    print(name)
    # userDB.conn.commit()
    cursor = userDB.cursor
    sql_by_name = "select * from custom where name = " + name
    print(sql_by_name)
    cursor.execute(sql_by_name)
    result = cursor.fetchone()
    print(result)
    if result:
        return_str = '客户名称: ' + str(result[1]) + '\n' + '号码 : ' + str(result[2]) + '\n' + '出生年月 : ' + str(result[3]) + \
                     '\n' + '年龄 : ' + str(result[4]) + '\n' + '第一次来店时间: ' + str(result[5]) + '\n' + '到店次数: ' + str(result[6]) + \
                     '次' + '\n' + '付款时间: ' + str(result[7]) + '\n' + '提车时间: ' + str(result[8]) + '\n' + '曾用车: ' + str(result[9]) + \
                     '\n' + '曾用车价格: ' + str(result[10]) + '\n' + '预购车型: ' + str(result[11]) + '\n' + '预购车型价格: ' + str(result[12]) + \
                     '\n' + '实提车型: ' + str(result[13]) + '\n' + '实提车价: ' + str(result[14]) + '\n' + '备注: ' + result[15]
    else:
        return_str = '未查询到 (' + name + ') 所绑定的客户信息'
    return return_str




