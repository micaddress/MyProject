# -*- coding: utf-8 -*-
import time, re, io
import sys
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# a = 1618553274
# localTime = time.localtime(a)
#
# strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
#
# print(strTime)
#
#
# a = '''<p data-pid="JUj2SbsS"><br><br>高晓松是名人，曾经有段时间，名人很吃得开，鲁迅先生说：“社会上崇敬名人，于是以为名人的话就是名言，却忘记了他之所以得名是那一种学问或事业。名人被崇奉所诱惑，也忘记了自己之所以得名是那一种学问或事业，渐以为一切无不胜人，无所不谈，于是乎就悖起来了。”<br><br>但是在今天，时代变了，大家尊重的是知识，是真理，而不是一个摇着扇子胡吹海侃的“名流”。<br><br>有些人没有搞明白一个简单的道理：人民群众不喜欢，你喜欢，你偏偏要给人民群众喂屎……人民群众是不乐意的，是要骂人的。<br><br>这和高晓松长得好不好，学问高不高没关系，这和他长期以来在人民群众心中留下的印象有关系。<br><br>如果说一个出租车司机，一个小区里的老大爷，天天不懂装懂胡吹海侃，满嘴暴论还假装人生导师，大家可以容忍。因为老师傅就这点水平，多说话多关心天下大事，说明他脑筋还不糊涂，没有老年痴呆，没有脱离社会，我们反而会鼓励他们多唠唠。<br><br>你一个油腻中年，社会名流，年纪不算大，钱也赚不算少，书也读的不少，偏偏也要学出租车司机，满嘴胡吹海侃，对听众对历史完全不负责任，谁还惯着你不成？<br><br>所以说，高晓松的地摊文学下架，对于人民群众来说，是一件大好事。<br><br>起码是一个好的开始。<br><br><br></p><figure data-size="normal"><noscript><img src="https://pic1.zhimg.com/v2-3832dac9aaf26ca7d93f4c10e9416fc0_720w.jpg?source=3af55fa1" data-caption="" data-size="normal" data-rawwidth="640" data-rawheight="385" class="origin_image zh-lightbox-thumb" width="640" data-original="https://pic2.zhimg.com/v2-3832dac9aaf26ca7d93f4c10e9416fc0_r.jpg?source=3af55fa1"></noscript><img src="data:image/svg+xml;utf8,&lt;svg%20xmlns='http://www.w3.org/2000/svg'%20width='640'%20height='385'&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="640" data-rawheight="385" class="origin_image zh-lightbox-thumb lazy" width="640" data-original="https://pic2.zhimg.com/v2-3832dac9aaf26ca7d93f4c10e9416fc0_r.jpg?source=3af55fa1" data-actualsrc="https://pic1.zhimg.com/v2-3832dac9aaf26ca7d93f4c10e9416fc0_720w.jpg?source=3af55fa1"></figure><p></p>'''
# # a = '<p>你好</p><br/><font>哈哈</font><b>大家好</b>'
# pattern = re.compile(r'<[^>]+>',re.S)
# result = pattern.sub('', a)
# print(result)

# action_text = 'asda打撒赞同fsdf'
# if '赞同' in action_text:
#     print('赞同' in action_text)
# a = {'a':'a1','b':'b1'}
# print(a.get('b'))
# print(str(a))
action_text = '关注了话题1'
if action_text in ['关注了话题','关注了圆桌']:
    print(1)