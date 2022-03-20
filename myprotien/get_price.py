# encoding='utf-8'
import sys
sys.path.append('D:/workspace/MyProject/')
from myprotien import get_myprotien_DB
import requests
import datetime
from lxml import etree
from xml.dom.minidom import parseString

creatien_url = 'https://www.myprotein.cn/sports-nutrition/creatine-monohydrate-powder/10530050.html'

creatien_response = requests.get(creatien_url)
creatien_tree = etree.HTML(creatien_response.text)

creatien_name = creatien_tree.xpath('//title/text()')[0].replace("\t","").replace("\n","").replace(" ","").split('|')[0]
print(creatien_name)

c_weight = creatien_tree.xpath("//li[@class='athenaProductVariations_listItem']/button//text()")
creatien_weight = ''
for i in range(len(c_weight)):
    cw = c_weight[i].replace('\n', '').replace('\t', '').replace(' ','')
    creatien_weight += cw
print(creatien_weight)

creatien_price = creatien_tree.xpath('//div[@class="athenaProductPage_productPrice_top"]//span[@class="productPrice_schema productPrice_priceAmount"]/text()')[0]
creatien_price = float(creatien_price)
print(creatien_price)

creatien_mark = creatien_tree.xpath("//div[@class='stripBanner']/a/text()")[0].replace("\t","").replace("\n","").replace(" ","")
print(creatien_mark)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

protien_url = 'https://www.myprotein.cn/sports-nutrition/impact-whey-protein/10530943.html?variation=10530960'

protien_response = requests.get(protien_url)
protien_tree = etree.HTML(protien_response.text)

protien_name = str(protien_tree.xpath("//div[@class='productName']/h1/text()")[0])
print(protien_name)

protien_weight = '5kg'

protien_price = protien_tree.xpath("//div[@class='athenaProductPage_productPrice_top']//span[@class='productPrice_schema productPrice_priceAmount']/text()")[0]
protien_price = float(protien_price)
print(protien_price)

protien_mark = protien_tree.xpath("//div[@class='stripBanner']/a/text()")[0].replace("\t","").replace("\n","").replace(" ","")
print(protien_mark)


sql_to_myprotien_price = '''insert into myprotien_price(
                                                        record_time,
                                                        name,
                                                        weight,
                                                        price,     
                                                        mark
                                                        ) values (%s,%s,%s,%s,%s)'''

get_myprotien_DB.cursor.execute(sql_to_myprotien_price,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                        creatien_name,
                                                        creatien_weight,
                                                        creatien_price,
                                                        creatien_mark))
get_myprotien_DB.cursor.execute(sql_to_myprotien_price,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                        protien_name,
                                                        protien_weight,
                                                        protien_price,
                                                        protien_mark))
get_myprotien_DB.conn.commit()
get_myprotien_DB.conn.close()

