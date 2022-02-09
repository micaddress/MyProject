# -- coding: utf-8 --

import  requests
from fake_useragent import UserAgent
import re
class douyin(object):
    def __init__(self):
        self.url='https://www.douyin.com/user/MS4wLjABAAAAInrzQwrrIn2mlqwThUiOWecnb4kBq6n34ctR_dQTJ2mFu-0nAgwMTjY5PIZ7llmr'
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 100):
            self.headers = {
                'User-Agent': ua.random
            }

    def get_html(self,url):
        response=requests.get(url,headers=self.headers)
        html=response.content.decode('utf-8')
        return html
    def parse_html(self,html):
        links=re.compile('open1\(\'(.*?)\',\'(.*?)\',\'\'\)').findall(html)
        for link in links:
            print('正在下载：'+link[0])
            host=link[1]
            r=requests.get(host,headers=self.headers)
            filename=link[0]
            with open('d:/1/'+filename+'.mp4','wb')as f:
                f.write(r.content)
    def main(self):
        start = int(input('输入开始：'))
        end = int(input('输入结束页：'))
        for page in range(start, end + 1):
            print('第%s页' % page)
            url = self.url.format(page)
            html = self.get_html(url)
            self.parse_html(html)
if __name__ == '__main__':
    spider = douyin()
    spider.main()





