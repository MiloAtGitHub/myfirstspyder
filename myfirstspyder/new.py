"""
这是我的第一个爬虫测试
"""
# import requests
# from fake_useragent import UserAgent
# import requests  # 导入requests包
#
#
#
# url = 'http://www.cntour.cn/'
# strhtml = requests.get(url)  # Get方式获取网页数据
# print(strhtml.text)
#
# ua = UserAgent()
# print(ua.ie)
import requests        # 导入requests包
from bs4 import BeautifulSoup
url = 'http://www.chinacs.org.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
# data1 = soup.select('')
# data = soup.select('#ul.dt_con1>li>a')
data = soup.find(text='a>')

print(data)

# #main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(1) > a
# #main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(2) > a
# #mainbox.clear10>div.sy_left>div.sy_xsdt>div.con>div.list>ul.dt_con1>li:> a

