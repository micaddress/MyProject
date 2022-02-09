# -- coding: utf-8 --
import requests
import os
from selenium import webdriver as web



# chrome_exe_path = __file__.split('/')[-1]
# chrome_exe_path = __file__.split(chrome_exe_path)[0]
# chrome_exe_path = chrome_exe_path + 'chromedriver.exe'
# web = webdriver.Chrome(chrome_exe_path)

# url = 'https://aweme.snssdk.com/aweme/v1/hotspot/video/preload/?hotword=%E5%8C%97%E4%BA%AC%E5%86%AC%E5%A5%A5%E4%BC%9A%E5%BC%80%E5%B9%95%E5%BC%8F&offset=0&count=2&source&sentence_id=539283&is_ad=0&is_trending=0&action_type=click&city_code&os_api=22&device_type=PCRT00&ssmix=a&manifest_version_code=140401&dpi=300&uuid=865333601713745&app_name=aweme&version_name=14.4.0&ts=1643974730&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi&update_version_code=14409900&channel=tengxun_1128_0112&_rticket=1643974732043&device_platform=android&iid=3738819694175837&version_code=140400&cdid=7cd97229-c655-467c-a860-207f8df58d98&openudid=87a6abfd66a1f543&device_id=4090663415317112&resolution=1600*900&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&mcc_mnc=46000'
url = 'https://www.163.com'
headers = {
    'Accept-Encoding': 'gzip'
    ,'tc_2021_now_client': 0
    ,'passport-sdk-version': 18
    ,'sdk-version': 2
    ,'X-SS-REQ-TICKET': 1643974732043
    ,'Cookie': 'install_id=3738819694175837; ttreq=1$d3bd9bd6f1393e1d00364a75b7bee97808bb3dec; odin_tt=446e41097fae6614ff70d21e8d6fce0f2b12fa6fb052dabbf074627ae964fd82b2e0ee0e9fee2db87727e11daac66e1a318134922e1ad4383f409c1f020a9e7e; passport_csrf_token_default=dd6d79826e35dd92a8b2569187bcebc9; MONITOR_WEB_ID=c794d1cd-3a7d-487b-bcef-8d57a8ceae4d'
    ,'X-Tyhon': 'umeDGpQxkw2Lfa1fjXbxPqhnlziIPaM4gUHwqW0='
    ,'X-Khronos': '1643974732'
    ,'X-Gorgon': '04040094000185986023163246bd60bf56677dad29c72d4f2087'
    ,'Host': 'aweme.snssdk.com'
    ,'Connection': 'Keep-Alive'
    ,'User-Agent': 'okhttp/3.10.0.1'
}
rep = requests.get(url=url, verify=False)
rep.encoding = rep.apparent_encoding
print(rep.text)
# options = web.ChromeOptions()
# # options.add_argument('--disable-blink-features=AutomationControlled')
# web = web.Chrome(options=options)
# # script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
# # web.execute_script(script)
# web.get(url)
# print(1)





