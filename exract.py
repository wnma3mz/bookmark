# coding: utf-8
import os
from bs4 import BeautifulSoup as bs
import json
with open(r'C:\Users\lu\Desktop\index.html', 'r', encoding='utf-8') as f:
    html = f.read()


lst = []
soup = bs(html, 'lxml')

lst = soup.find_all(class_="codelist codelist-desktop cate1")
lst = soup.find_all("a")


string = """
<div class="col-sm-3">
    <div class="xe-widget xe-conversations box2 label-info"
        onclick="window.open('{}', '_blank')" data-toggle="tooltip"
        data-placement="bottom" title="" data-original-title="{}">
        <div class="xe-comment-entry">
            <a class="xe-user-img">
                <img src="{}" class="img-circle" width="40">
            </a>
            <div class="xe-comment">
                <a href="#" class="xe-user-name overflowClip_1">
                    <strong>{}</strong>
                </a>
                <p class="overflowClip_2">{}</p>
            </div>
        </div>
    </div>
</div>
"""
head_div = """  
<h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id="{}"></i>{}</h4>
<div class="row">
"""

with open("t.html", "w", encoding='utf-8') as f:
    for x in lst:
        item = bs(x).a
        href = item.attrs["href"]
        icon = item.attrs["icon"] if "icon" in item.attrs else "https://www.google.com/s2/favicons?domain=" + href.split('/')[2]
        title = item.text
        f.write(string.format(href, href, icon, title, title) + "\n\n")

assert 1==2
with open('1\\BookMarks', 'r', encoding='utf-8') as f:
    d = json.load(f)

d = d['roots']['bookmark_bar']
s = d['children'][2]['children']
head_title='其他工具'
with open('1.txt', 'w', encoding='utf-8') as f:
    for item_children in s:
        if 'children' in item_children.keys():
            head_title = item_children['name']
            f.write(head_div.format(head_title, head_title))

            for item in item_children['children']:
                url = item['url']
                img_url = "https://www.google.com/s2/favicons?domain=" + item['url'].split('/')[2]
                title = item['name']
                text = item['name']
                f.write(string.format(url, url, img_url, title, text))
            f.write('</div>')

"""
with open('1.txt', 'w', encoding='utf-8') as f:
    for head in lst:

        head_title = head.h2.text
        print(head_title)
        f.write(head_div.format(head_title, head_title))
        print(head_div.format(head_title, head_title))

        for item in head.find_all('a'):
            url = item['href']
            img_url = item.img['src']
            title = item.h4.text
            text = item.strong.text
            f.write(string.format(url, url, img_url, title, text))
            print(string.format(url, url, img_url, title, text))
        
        f.write('</div>')
        print('</div>')
"""
