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
    echostr = request.args.get('echostr')

    if not all([signature, timestamp, nonce, echostr]):
        abort(400)

    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    tmp_str = ''.join(li)
    tmp_str = tmp_str.encode('utf8')
    sign = hashlib.sha1(tmp_str)
    sign = sign.hexdigest()
    print('=' * 100)
    print('echostr:' + echostr)
    print('nonce:' + nonce)
    print('timestampe:' + timestamp)
    print('signature:', signature)
    print('sign:     ', sign)
    print('=' * 100)
    if signature != sign:
        abort(403)
    else:
        return echostr
if __name__ == '__main__':
    app.run(port=3001, debug=True)