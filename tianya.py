import urllib
from lxml import etree
import socket

def loadpage(i):
    for i in range(i):
        i=i+1
        url="http://bbs.tianya.cn/m/post-house-252774-"+str(i)+".shtml"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        req=urllib.request.Request(url=url,headers=headers)
        html=urllib.request.urlopen(req).read()
        text=etree.HTML(html)
        loadword(text)

def loadword(text):
    word_list=text.xpath('//div[@data-user="kkndme"]/div/div[@class="reply-div"]')
