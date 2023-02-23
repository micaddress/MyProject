# -- coding: utf-8 --
from flask import Flask, request, abort
import gongzhonghao.get_custmor_info as getinfo
import hashlib
import xmltodict
import time
import os
import openai

app = Flask(__name__)
app.url_map.default_subdomain = 'mic'
app.config['SERVER_NAME'] = 'mykorea02.ml'
# app.register_blueprint(public,subdomain='static')'
WECHAT_TOKEN = 'michael_chatGPT'
openai.api_key = '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'
count = 0
count = 0

@app.route('/chatGPT_final', methods=['GET', 'POST'])
def wechat():

    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    tmp_str = ''.join(li)
    tmp_str = tmp_str.encode('utf8')
    sign = hashlib.sha1(tmp_str)
    sign = sign.hexdigest()
    if signature != sign:
        abort(403)
    else:
        if request.method == 'GET':
            echostr = request.args.get('echostr')
            return echostr
    if request.method == 'POST':
        xml_str = request.data
        if not xml_str:
            abort(400)
        xml_dict = xmltodict.parse(xml_str)
        xml_dict = xml_dict.get('xml')
        msg_type = xml_dict.get('MsgType')

        if msg_type == 'text':

            cont = xml_dict.get('Content')

            prompt = cont
            model = 'text-davinci-003'
            # model = 'text-ada-001'
            response = openai.Completion.create(
                model=model,
                # top_p=1,
                # engine=model,
                prompt=prompt,
                max_tokens=100,
                temperature=0,
                n=1,
                stop=None
            )
            # results = ''
            # for result in response.choices:
            # print('----------------')
            # results += result.text

            # search_type_list = cont.split(' ')
            # if len(search_type_list) == 3:
            #     search_type = cont.split(' ')[0]
            #     if search_type == '查询':
            #         search_content_type = cont.split(' ')[1]
            #         search_content = cont.split(' ')[2]
            #         if search_content_type == '手机':
            #             return_content = getinfo.get_info_by_phone(search_content)
            #         elif search_content_type == '姓名':
            #             return_content = getinfo.get_info_by_name(search_content)
            # else:
            #     return_content = '查询格式错误 请重新输入' + '\n' + '正确格式:查询(空格)手机(空格)查询内容'
            print('---------------')
            return_content = response.choices[0].text.strip()
            print(return_content)
            print('===============')
            resp_dict = {
                'xml': {
                    'ToUserName': xml_dict.get('FromUserName'),
                    'FromUserName': xml_dict.get('ToUserName'),
                    'CreateTime': int(time.time()),
                    'MsgType': 'text',
                    'Content': return_content
                }
            }
        else:
            resp_dict = {
                'xml': {
                    'ToUserName': xml_dict.get('FromUserName'),
                    'FromUserName': xml_dict.get('ToUserName'),
                    'CreateTime': int(time.time()),
                    'MsgType': 'text',
                    'Content': 'I love you'
                }
            }
        # 字典转化为字符串
        resp_xml_str = xmltodict.unparse(resp_dict)
        return resp_xml_str

    return 'how are you1'


if __name__ == '__main__':
    command ='''kill -9 $(netstat -nlp | grep :'''+str(80)+''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
    print(command)
    os.system(command)
    app.run(host='0.0.0.0', port=80, debug=True)


