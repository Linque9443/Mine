import requests
import re

HEADER = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
def parse_page(url):

    response = requests.get(url,headers=HEADER)
    html = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',html,re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',html,re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',html,re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',html,re.DOTALL)
    # print(title)
    # print(chaodai)
    # print(zuozhe)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>','',content)
        contents.append(x.strip())

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
    for x in range(1,3):
        url = "https://www.gushiwen.org/default_%d.aspx" %x
        parse_page(url)


if __name__ == '__main__':
    main_page()
