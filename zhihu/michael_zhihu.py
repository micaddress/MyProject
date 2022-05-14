# -*- coding: utf-8 -*-
import requests
import random
import sys
import io
import time
import re
import os
import csv
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


class fuckyou1450:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }
        self.count = 0
        self.all_count = 0

    def get_user_detail(self, next_url, username, userid, path, csv_writer):
        user_detail_json = requests.get(url=next_url, headers=self.headers)
        jsons = user_detail_json.json()
        next_datas = jsons['data']
        for data in next_datas:
            list_content = []
            self.count += 1
            self.all_count += 1
            action_text = data.get('action_text')
            if action_text in [
                '关注了话题',
                '关注了圆桌',
            ]:
                title = data.get('target').get('name')
            else:
                if data.get('target'):
                    a = data.get('target')
                    if a:
                        b = a.get('question')
                        if b:
                            title = b.get('title')
                        else:
                            title = a.get('title')
            create_time = data.get('created_time')
            create_time = time.localtime(create_time)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
            create_time = str(create_time).encode('utf-8').decode('utf-8')

            # list_content.append(username)
            # list_content.append(userid)
            list_content.append(create_time)
            list_content.append(action_text)
            list_content.append(title.encode('utf-8').decode('utf-8'))
            content = ''
            if '回答了问题' in action_text:
                content = data.get('target').get('content')
                pattern = re.compile(r'<[^>]+>', re.S)
                content = pattern.sub('', content)
                list_content.append(content)
            try:
                csv_writer.writerow(list_content)
            except Exception as e:
                print(e)
            if '赞同' in action_text:
                print(self.all_count,self.count,username,userid,create_time,action_text,title,)
            else:
                print(self.all_count,self.count,username,userid,create_time,action_text,title,)

        next_flag = jsons.get('paging').get('is_end')
        if not next_flag:
            sleep_time = 3
            random_int = random.randint(1,sleep_time)
            for i in range(0,random_int):
                time.sleep(1)
                print(random_int - i)
            self.get_user_detail(jsons.get('paging').get('next'),username,userid,path,csv_writer)
        else:
            print(username, '的信息爬取结束。。。共获取 ', self.count, ' 条', username, '数据')
            self.count = 0

    def get_data(self, user_map):
        for username in user_map:
            userid = user_map.get(username)
            url = 'https://www.zhihu.com/people/' + userid
            resp = requests.get(url=url, headers=self.headers)
            content = resp.text
            next_url = re.search(r'"previous":"(.*)","next":',content).group()
            next_url = next_url.split('"previous":"')[-1].split('","next":')[0].encode('utf-8').decode("unicode_escape")
            path = "D:\\1450\\" + username + '.csv'
            if os.path.exists(path):
                os.remove(path)
            with open(path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(['用户名:',username,'用户ID:',userid])
                self.get_user_detail(next_url, username, userid, path, csv_writer)


if __name__ == '__main__':
    user_maps = {
        # '晨曦': 'chen-xi-54-6-85-50',# 1450
        # 'mua丽塔': 'muali-ta',# 1450
        # 'eijcoe': 'trump-61-77', # 1450
        # '綦巾茹藘': 'da-hao-ren-74-58', # 1450
        '1分钟妙招小窍门': 'sao-nian-xian-feng-dui-72', # 1450
    }
    getdata = fuckyou1450()
    getdata.get_data(user_maps)


