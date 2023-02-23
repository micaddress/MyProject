# encoding='utf-8'
# import itchat, re
# import wechat.get_user_info_DB as userDB
import openai

openai.api_key = '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'
while 1:
    prompt = input('请输入：')
    model = 'text-davinci-003'

    response = openai.Completion.create(
        model=model,
        # top_p=1,
        # engine=model,
        prompt=prompt,
        max_tokens=1000,
        # temperature=0.9,
        # n=10
    )
    # print(response)
    for result in response.choices:
        print('----------------')
        print(result.text)
# print(openai.api_key)

# itchat.auto_login(hotReload=True)
# qunliao = itchat.get_chatrooms(update=True)
# # reply_username = '@bff53d4c49d010e4233dc38ecceda2cea454d33af9c595f4c5fc322c8c63ec01' # 爸爸
# # reply_username = '@91f00211108e1821f51530e04f29c40293817b5a24a369a35eb395ea178a3446'  # 妈妈
# reply_username = '@22d0b325219659bf429da0e63c7a1014042ea7cd7b4e71820f01a791f3d505b1'  # PonPon
# friends_list = itchat.get_friends(update=True)
# i = 0
#
#
# @itchat.msg_register(itchat.content.TEXT)
# def get_user_message(msg):
#
#     from_username = msg['FromUserName']
#     from_content = msg['Text']
#     check_flag = from_content.split(' ')[0]
#     if from_username == reply_username and check_flag == '查询':
#         phone = from_content.split(' ')[-1]
#         if len(phone) != 11:
#             return '号码位数不对，请输入正确的手机号码'
#         return_str = get_info_by_phone(phone)
#         if return_str:
#             return return_str
#         else:
#             return '未查询到此号码所关联的客户信息'
#
#
# def get_info_by_phone(phone):
#     cursor = userDB.cursor
#     sql_by_phone = ''' select * from custom where phone = ''' + str(phone)
#     cursor.execute(sql_by_phone)
#     result = cursor.fetchone()
#     if result:
#         return '客户名称: ' + result[0] + '\n' + '号码 : ' + str(result[1]) + '\n' + '出生年月 : ' + str(result[2]) + \
#                '\n' + '年龄 : ' + str(result[3]) + '\n' + '第一次来店时间: ' + str(result[4]) + '\n' + '到店次数: ' + str(result[5]) + \
#                '次' + '\n' + '付款时间: ' + str(result[6]) + '\n' + '提车时间: ' + str(result[7]) + '\n' + '曾用车: ' + str(result[8]) + \
#                '\n' + '曾用车价格: ' + str(result[9]) + '\n' + '预购车型: ' + str(result[10]) + '\n' + '预购车型价格: ' + str(result[11]) + \
#                '\n' + '实提车型: ' + str(result[12]) + '\n' + '实提车价: ' + str(result[13]) + '\n' + '备注: ' + result[14]
#     else:
#         return None
#
#
# def get_right_phone_No(number):
#     # number = input("请输入一个手机号：")
#     flag = True
#     if re.match(r'1[3,4,5,7,8]\d{9}', number):
#         print("您输入的的手机号码是：\n", number)
#         # 中国联通：
#         # 130，131，132，155，156，185，186，145，176
#         if re.match(r'13[0,1,2]\d{8}', number) or \
#                 re.match(r"15[5,6]\d{8}", number) or \
#                 re.match(r"18[5,6]", number) or \
#                 re.match(r"145\d{8}", number) or \
#                 re.match(r"176\d{8}", number):
#             print("该号码属于：中国联通")
#         # 中国移动
#         # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
#         # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
#         elif re.match(r"13[4,5,6,7,8,9]\d{8}", number) or \
#                 re.match(r"147\d{8}|178\d{8}", number) or \
#                 re.match(r"15[0,1,2,7,8,9]\d{8}", number) or \
#                 re.match(r"18[2,3,4,7,8]\d{8}", number):
#             print("该号码属于：中国移动")
#         else:
#             # 中国电信
#             # 133,153,189
#             print("该号码属于：中国电信")
#     else:
#         print("请输入正确的手机号")
#         flag = False
#     return flag
#
#
# itchat.run()

