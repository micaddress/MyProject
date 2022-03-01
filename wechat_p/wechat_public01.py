# -- coding: utf-8 --
from flask import Flask, request, abort
import hashlib
import xmltodict
import time
WECHAT_TOKEN = 'micaddress'
app = Flask(__name__)


@app.route('/connect', methods=['GET', 'POST'])
def wechat():
    # 接受微信服务器发送的参数
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    # echostr = request.args.get('echostr')

    if not all([signature, timestamp, nonce]):
        abort(400)

    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    tmp_str = ''.join(li)
    tmp_str = tmp_str.encode('utf8')
    sign = hashlib.sha1(tmp_str)
    sign = sign.hexdigest()
    print('=' * 100)
    # print('echostr:' + echostr)
    print('nonce:' + nonce)
    print('timestampe:' + timestamp)
    print('signature:', signature)
    print('sign:     ', sign)
    print('=' * 100)
    if signature != sign:
        abort(403)
    else:
        if request.method == 'GET':
            echostr = request.args.get('echostr')
            if not echostr:
                abort(400)
            return echostr
        elif request.method == 'POST':
            xml_str = request.data
            if not xml_str:
                abort(400)
            xml_dict = xmltodict.parse(xml_str)
            xml_dict = xml_dict.get('xml')

            msg_type = xml_dict.get('MsgType')
            if msg_type == 'text':
                resp_dict = {
                    'xml': {
                        'ToUserName':xml_dict.get('FromUserName'),
                        'FromUserName':xml_dict.get('ToUserName'),
                        'CreateTime':int(time.time()),
                        'MsgType':'text',
                        'Content':xml_dict.get('Content')
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
            resp_xml_str = xmltodict.unparse(resp_dict)
            return resp_xml_str


if __name__ == '__main__':
    app.run(port=3000, debug=True)