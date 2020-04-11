"""
requests 测试
"""

import requests
from fake_useragent import UserAgent
import os
from bs4 import BeautifulSoup
import lxml


def getwebpage(url, param=None, **kwargs):
    """
    :param url: 网址
    :param param: 参数
    :param kwargs: 其他参数
    :return:
    """
    ua = UserAgent()     # 伪造头部信息
    headers = {'User-Agent': ua.random}   # 使用随机头部信息构造headers
   # print(ua.ie)

    try:
        r = requests.get(url, params=param, headers=headers)   # 获取页面内容
        r.raise_for_status()    # 异常检测
        r.encoding = r.apparent_encoding       # 为正确显示编码，使用apparent_encoding为response对象encoding赋值
        head = r.headers        # 获取页面头部信息
        request = r.request.headers  # 获取request的头部信息
        # print(r.request.url)    # 获取request的url信息，检查参数加载是否成功
        result = r.text
        soup = BeautifulSoup(result, 'html.parser')   # 用html.parser解析r.text
       # print(result)
        print(soup.a)       # 查询<a>标签
        print(soup.a.attrs)     # 标签属性 返回一个dict对象
        print(soup.a.string)  # 标签中文本部分
        print(type(soup.a.string))  # soup.a.string的数据类型为bs4.element.NavigableString

        return result          # 返回页面内容
    except requests.RequestException:      # 异常处理
        return "err"


def getwebpic(url, param=None, **kwargs):
    """ 获得图片并存在本地"""
    dir = "./pic/"
    path = dir + url.split('/')[-1]    # 拼接dir和文件名称，新建图片文件
    ua = UserAgent()     # 伪造头部信息
    headers = {'User-Agent': ua.random}   # 使用随机头部信息构造headers
   # print(useragent.ie)
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(path):
            try:
                r = requests.get(url)   # 获取页面内容
                r.raise_for_status()    # 异常检测
                # r.encoding = r.apparent_encoding       # 为正确显示编码，使用apparent_encoding为response对象encoding赋值
                head = r.headers        # 获取页面头部信息
                request = r.request.headers  # 获取request的头部信息
                # print(r.request.url)    # 获取request的url信息，检查参数加载是否成功
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("File done。")
              #  return r.content          # 返回页面内容
            except requests.RequestException:      # 异常处理
              #  return "err"
                print('Fail')
        else:
            print('文件已存在')
    except:
        print('Someting is wrong.')


if __name__ == "__main__":
    requesturl = "http://www.chinacs.org.cn/"
    keyword = {}
    kwaggr = ''
    pagetext = getwebpage(requesturl)
 #   pic = getwebpic("http://www.chinacs.org.cn/upload/202003/20200310131409753.jpg")


# http://www.chinacs.org.cn/upload/202003/20200310131409753.jpg
  #  print(pagetext)
