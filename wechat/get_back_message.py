# encoding='utf-8'
import itchat
import time
from itchat.content import *

itchat.auto_login(hotReload=True)
friends_list = itchat.get_friends(update=True)
# itchat.send('Hello,filehelper', toUserName='filehelper')  # 文件传输助手

back_msg_path = 'd:\\back_msg'+'\\'

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
    info = msg['Content']
    file_name = msg['FileName']
    reback_time = msg['CreateTime']

@itchat.msg_register([NOTE, ])
def backed_msg(ch_msg):
    global types
    global info
    global file_name
    global reback_time
    if '撤回了一条消息' in ch_msg['Content']:
        if types == RECORDING:
            info(back_msg_path, file_name)
            itchat.send(info, toUserName='filehelp')
        elif types == 'Text':
            # with open(back_msg_path + '文本撤回.txt', 'a') as f:
            #     f.write(info)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(reback_time))
            itchat.send(create_time + '--' +ch_msg['Text'] + ':' + info, toUserName='filehelper')


itchat.run()

