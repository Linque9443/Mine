import requests
import re

HEADER = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
def parse_page(url):

    response = requests.get(url,headers=HEADER)
    html = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',html,re.DOTALL) #爬取标题
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',html,re.DOTALL) #爬取朝代
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',html,re.DOTALL) #爬取作者
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',html,re.DOTALL) #爬取诗文，糅合了一些标签和换行符
    contents = [] #整合成一个列表
    for content in content_tags:
        x = re.sub(r'<.*?>','',content).strip() #用sub函数把无用标签替换成空白字符,并用strip函数删除空白字符所占用的空间
        contents.append(x) # 添加进列表

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('————'*40)

def main_page():
    #只爬取两页
    for x in range(1,3):
        url = "https://www.gushiwen.org/default_%d.aspx" %x
        parse_page(url)


if __name__ == '__main__':
    main_page()
