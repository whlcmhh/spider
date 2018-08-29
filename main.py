import urllib.request,urllib.parse
from lxml import etree
import socket
socket.setdefaulttimeout(10.0)


def loadpage(url):


    req=urllib.request.Request(url=url)
    try:
        html=urllib.request.urlopen(req).read()
    except error.HTTPError as e:
        print(e.code())



    # with open('test.html','wb') as f:
    #     f.write(html)

    content=etree.HTML(html)

    # link_list=content.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    link_list = content.xpath('//a[@class="j_th_tit "]/@href')
    for link in link_list:

        full_link='http://tieba.baidu.com'+link
        loadImage(full_link)

def loadImage(url):

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req=urllib.request.Request(url=url,headers=headers)
    html=urllib.request.urlopen(req).read()
    content=etree.HTML(html)
    link_list=content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)

def writeImage(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req=urllib.request.Request(url=url,headers=headers)
    image=urllib.request.urlopen(req).read()
    filename=url[-10:]
    with open('img/'+filename,'wb') as f:
        f.write(image)
    print('成功下载'+filename)

def tiebaSpider(url,beginPage,endPage):

    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fullurl=url+'&pn='+str(pn)
        loadpage(fullurl)

if __name__=='__main__':
    kw=input('请输入贴吧名')
    beginPage=int(input('请输入开始页数:'))
    endPage=int(input('请输入结束页数:'))

    url='http://tieba.baidu.com/f?'
    kw=urllib.parse.urlencode({"kw":kw})
    fullurl=url+kw
    tiebaSpider(fullurl,beginPage,endPage)



