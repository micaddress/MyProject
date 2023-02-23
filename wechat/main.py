from flask import Flask, request
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import TextReply
import requests

app = Flask(__name__)

TOKEN = "���ں�Token"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ��дAPI_KEY'
}


@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = TOKEN
        try:
            check_signature(token, signature, timestamp, nonce)
        except InvalidSignatureException:
            # �����쳣��������
            return "У��ʧ��"
        # У��ɹ�
        return echostr
    if (request.method == "POST"):
        xml_str = request.data
        # ����xml��ʽ����
        msg = parse_message(xml_str)
        xml_str = request.data
        # ����xml��ʽ����
        msg = parse_message(xml_str)
        # 1.Ŀ���û���Ϣ
        target = msg.target
        # 2.�����û���Ϣ
        source = msg.source
        # 3.��Ϣ����
        msgType = msg.type
        # 4.��Ϣ����
        msgCcontent = msg.content

        print(msgCcontent)

        reply = TextReply()
        reply.source = target
        reply.target = source
        # answer = chat.ask(msgCcontent)[0]



        json_data = {
            'model': 'text-davinci-003',
            'prompt': msgCcontent,
            'max_tokens': 2000,
            'temperature': 0
        }

        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
        reply.content = response.json()['choices'][0]['text'].strip()
        print(reply.content)
        # ��װ��XML��ʽ������
        xml = reply.render()
        return xml


if __name__ == '__main__':
    app.run(port=80)