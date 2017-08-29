from bs4 import BeautifulSoup
import requests
import os
print("网站地址:http://www.jdlingyu.wang/\n文件会保存到D盘J_site文件夹下。")

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
while True:
	url = input("页面编号:")
	path = "D:/J_site/"
	html_url = requests.get(url, headers=header)
	soup = BeautifulSoup(html_url.text, "html.parser")
	link = soup.find("div", class_="main-body").find_all("a")
    # 获取一个页面的图片链接集
	title = soup.find("div", class_="main-header").find_all("h2", class_="main-title")[0].text
    # 得到当前页面的标题，来创建文件夹
	page = len(link)
	if os.path.exists(path + str(title)) == True:
		print("文件夹已经存在")
		continue
	os.makedirs(path + str(title))
    # 建立文件夹
	os.chdir(path + str(title))
	print("开始爬取:" + str(title))
    # 跟换到新建的文件夹中
	for i in range(page):
		pic_link = link[i]["href"]
		Get_pic = requests.get(pic_link, headers=header)
		f = open(str(i+1) + '.jpg', 'wb')
		f.write(Get_pic.content)
		f.close()
	print("完成爬取:" + str(title))