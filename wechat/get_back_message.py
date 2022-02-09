# encoding='utf-8'
import itchat
import time
import os
from itchat.content import *

itchat.auto_login(hotReload=True)
friends_list = itchat.get_friends(update=True)
# itchat.send('Hello,filehelper', toUserName='filehelper')  # 文件传输助手

back_msg_path = r'd:/back_msg/'
if not os.path.exists(back_msg_path):
    os.mkdir(back_msg_path)

types = None
info = None
file_name = None
reback_time = None


@itchat.msg_register([
                      TEXT,
                      MAP,
                      CARD,
                      PICTURE,
                      RECORDING,
                      VIDEO,
                      FRIENDS,
                      ])
def resave_msg(msg):
    global types
    global info
    global file_name
    global reback_time
    types = msg['Type']
    info = msg['Text']
    file_name = msg['FileName']
    reback_time = msg['CreateTime']


@itchat.msg_register([NOTE])
def backed_msg(ch_msg):
    global types
    global info
    global file_name
    global reback_time
    if '撤回了一条消息' in ch_msg['Text']:
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(reback_time))
        if types == PICTURE:
            info(back_msg_path + file_name)
            file = '@fil@%s' % (back_msg_path + file_name)
            pict = ch_msg['Text'].replace('条消息', '张图片')
            print(create_time + '--' + pict)
            itchat.send(create_time + '--' + pict, toUserName='filehelper')
            itchat.send(msg=file, toUserName='filehelper')
        elif types == RECORDING:
            info(back_msg_path + file_name)
            file = '@fil@%s' % (back_msg_path + file_name)
            pict = ch_msg['Text'].replace('消息', '语音')
            print(create_time + '--' + pict)
            itchat.send(create_time + '--' + pict, toUserName='filehelper')
            itchat.send(msg=file, toUserName='filehelper')
        elif types == 'Text':
            print(create_time + '--' + ch_msg['Text'] + ':' + info)
            itchat.send(create_time + '--' + ch_msg['Text'] + ':' + info, toUserName='filehelper')


itchat.run()

