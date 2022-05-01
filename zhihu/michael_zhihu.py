# -*- coding: utf-8 -*-
import requests
import sys
import io
from lxml import etree
import time
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


class fuckyou1450:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }
        self.count = 0

    def get_user_detail(self, next_url, username):
        user_detail_json = requests.get(url=next_url, headers=self.headers)
        jsons = user_detail_json.json()
        # print(jsons)
        datas = jsons['data']
        # print('*'*150)
        for data in datas:
            self.count += 1
            title = ''
            content = ''
            try:
                title = data['target']['question']['title']
            except Exception as e:
                title = data['target']['title']
                # print(title)
                # print(e)
            # title = data['target']['question']['title']
            action_text = data['action_text']
            create_time = data['created_time']
            create_time = time.localtime(create_time)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
            if '赞同' in action_text:
                content = data['target']['content']
                pattern = re.compile(r'<[^>]+>',re.S)
                content = pattern.sub('', content)
                print(self.count,username,create_time,action_text,title)
                # print('内容:',content)
            else:
                print(self.count,username,create_time,action_text,title)
        next_flag = jsons['paging']['is_end']
        if not next_flag:
            # for i in range(2):
            #     time.sleep(1)
            #     print(2-i)
            time.sleep(1)
            self.get_user_detail(jsons['paging']['next'],username)
        else:
            print(username, '的信息爬取结束。。。共获取 ', self.count, ' 条', username, '数据')

    def get_data(self, user_map):
        for user in user_map:
            url = 'https://www.zhihu.com/people/' + user_map[user]
            resp = requests.get(url=url, headers=self.headers)
            content = resp.text
            next_url = re.search(r'session_id=(.*)}},"answersByUser',content).group()
            next_url = next_url.split('"next":"http:')[-1].split('"}},"answersByUser')[0].encode('utf-8').decode("unicode_escape")
            next_url = "https:" + next_url
            # print(next_url)
            self.get_user_detail(next_url, user)


if __name__ == '__main__':
    user_maps = {
        '晨曦': 'chen-xi-54-6-85-50',
        # 'mua丽塔': 'muali-ta',
        # 'Michael': 'michael-23-3-35',
    }
    getdata = fuckyou1450()
    getdata.get_data(user_maps)

# html = etree.HTML(resp.text)
# print(html)
