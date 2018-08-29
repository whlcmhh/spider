from lxml import etree
from urllib import request



# with open('test.html',"rb") as f:
#     html=f.read()
# print(html)
# req=request.Request('http://tieba.baidu.com/f?kw=%BF%B9%D1%B9&fr=ala0&tpl=5')
# html=request.urlopen(req).read()
# with open('test.html','wb') as f:
#     f.write(html)

with open('test.html','rb') as f:
    html=f.read()

content=etree.HTML(html)

print(content)
# link_list = content.xpath("//a[@class='j_th_tit ']/@href")
link_list = content.xpath('//a[@class="j_th_tit "]/@href')
print(link_list)
