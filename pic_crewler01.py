#!/usr/bin/env  python3
#coding=utf-8

from bs4 import BeautifulSoup
import requests

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
# http请求头
url = "http://www.zhangzishi.cc/20170730mt.html"
html_url = requests.get(url,headers = header)
html_url.encoding = 'UTF-8'    #没有定义页面编码的情况下可能出现乱码，查找页面的编码格式来设置
soup = BeautifulSoup(html_url.text,"html.parser")
get_head = soup.find('header', class_='article-header').find_all('a')[0]  #获取标题，来命名文件（现阶段，只相对于没有建立文件夹）
pic_name = get_head.text
pic = soup.find_all('img',class_ ='M_cur_zoom_out') #获取图片所在的内容
length = len(pic)   #定义数量
for i in range(length):
    pic_link = pic[i]['src']
    get = requests.get(pic_link,headers = header)
    f = open( pic_name+'_'+str(i)+ '.jpg', 'wb')
    f.write(get.content)
    f.close()



