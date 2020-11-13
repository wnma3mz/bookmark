# coding: utf-8
import os
from bs4 import BeautifulSoup as bs
import json
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = """
<DT><A HREF="https://stackedit.io/editor" ADD_DATE="1582983230" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABrUlEQVQ4jY2QwWsTQRSHvxnHbheWTBpoKdRqiIIgJZQIyUEaUgnexEsPFT35J5iD6CUgerXoqQiC0EMFT156ESFYPCSnaah4kB5CDZGV0saq26ybrLeaUrvuwMB7zHwf7/fE2mcSlxUPJizuAOPEO7tmd3H5jbv6UJ32WWr63MqICx8yk0/mUZcEiBO4EILNcO3TT1P7ulgJGWgJLACWpe9dxbou/P40L1fes7OnefW6AacyQ/c8WDfEWOrmPDAi4LYEEgCjapper0ez2cTzPIwx+L5Pv98/NkfSPiwdNfzQaDSo1WoAuK6LlJJut0sqlTpxGUcE+XyeTqeD4zi4rks6nUZrHbnNI4J6vY4xBtu28TyPVqtFNpuNnEAON8VikWQySaVSQWtNtVqNhI8JgiAgl8sBUCgUIsF/RlBKUS6XASiVSrEE8v9fYgr2D0xsqN39Wx9GGH33eJ0zv+ZwpqLp/W3a366sY1+bAxBvP/J98gtbMxtkiRlpINTg0cXtzR8jE2fl2B7PZzY4FxcGkGEg727NTiV+t1+I8BkJDniKYIEQJ6Zjh5AVPO7/ASh2h7d7wT7+AAAAAElFTkSuQmCC">StackEdit – Editor</A>
<DT><A HREF="https://xiezuocat.com/#/editor?docId=473913&new=true" ADD_DATE="1584017824" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACEklEQVQ4jbWTT0hUURTGv3Pufe9N7yVTOLiwoj/jH6ZFuglsIahIJKE5i6Sdq2gVJO4KcQw3LWoZQgRtIghqgkJIiilq+gNtgmRiokhECyqR0Rln3szc02LSoRhJiH6be+/h49zvu5wL/Cdoi7VayFaFmxM++rChqe+Ds37e15UItPQnQrW0XN3GGACaB5PtTjA0q9xv8UrttgrU29Pa2f6+eTDZXnFYdcm/9xNSGpcBExJRfY29HcPAUBlCQSG4KK5lABJgYqMBVW+PmUg0eQraumVKayazkiWt9YKIaXNth6H1Lm27HQXfJD/GD7/7w8G4tA48rxPCBIGQ9/0vudxKxnLqdge2eRfS97u/E+iIDjRMWVy62dj/xl2PwYAwQEIWj7B2W8QUs8oO9CjtTJqygQKdCQ8kmgTy0l+dX2XlHArqwtlKFGEGyDQff3aAgHO/El39FO9ML7E/JZKfJe15WltX0vHOtwRcAxjCNBo+8XQPQIYBQDk8RtrbIaXsXGY5dwmIMZ4MrUJovFzOG4bV1xp9cWytXLhoSrlFpb2Qre3zAMD7o6/bABomYgJkcuFx7w9gHECM56Z77pApzqhAvWbWY5/vdS8T0SRYkcCcbjr56qBW+cIiu86MKWaXUncf3ag8DpnKGoNv9Ihl8jtF8AAAUqn565HI3i4i7eUz5a9bHU7+u2RTNqbu3/9ILX4CAbm/BOux1ucAAAAASUVORK5CYII=">秘塔写作猫</A>
<DT><A HREF="https://btsynckeys.herokuapp.com/" ADD_DATE="1585147596">BTSyncKeys</A>
<DT><A HREF="http://md.aclickall.com/" ADD_DATE="1586674011" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACzUlEQVQ4jQXBS28bRQAA4NmZnV2vvX7GXjuNk7ppErBC2oRWlVAkeoDCAXGAW7nyL3rsP+BE7z1w49ZT20uQEFKFqKgiakep49j7sNPs27M7OzuzfJ/05OHed49/vP/1l7mKRBmregUqCo1ibrvAcnnB8e0e7DUFF4BzqSjkhtEanZ+16tWtO0MZ6eb4HXPCXlAglodSHp68C2dO79t77Z+/4QgVuUA/Pbr3ya2beRTn7nW2mP369Nkvz3979edf+nix8+AAbHfd/y5mv/+ReaFx/BnPGHr86EEQk5SDylrVf3t+dwE/3xjMi5UdLjdGUWWrwzuaYy2mJ2/r7bpxtIt+OD4ChZQmJM1okeRKCa2j8jFullfZ7P38wrHMs4nr+Amj8dQKE1fWdY3EQS6o79LN9a4+aM8uTeeNGZluXDDv37MqRABBCUlXfmBwKpPAIymhjEoAzOc2FjmhadSRPgyAPyFrOWRACAEh54pUqLUyOixhjgTjOc3SVRzZ9mLp+klM5DLiNWnCUzfhSsbXVLV00Hk5/SBXDD2XuHvlYUXGlVKS0euYtMoYFqCtaWGL2jjFDNUE6A5anchD33+xfWHa8+XHouDDfv/h0TDnDEMJSSJLGS5AU8YlJE088tEK63UVHe82/x5dmi6RgABC6BDdutFBgnu+T7Occ1BRcKOpq53adBlYYYj2u5XLhQsRIklWq6qaAM7Cj6IwTWjKhL+iFEoc4+uY+HLRWjdkLIOvDnc6RsO89u7u7b6fecye8jRjnPmEKhCuoiQACmHFpzd79/dvw+3BjTsHe/3+xuZmL1Prz16/IY0tY2do+ZQVKGEAVvTtzf444JYdjMdT+XB/iASnWW40m89PTsmKWgnFnLVLJaRoQFNUvfrin/NTO5hcAStO5LbeTFNSknNJ1Ww3ULAyMh2kFgfd/iWGs+XV6WjkRKmuQgih0Br/A9TanknwFp6pAAAAAElFTkSuQmCC">Md2All</A>
<DT><A HREF="http://www.home-for-researchers.com/paper/index.html#/" ADD_DATE="1590500565" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACoElEQVQ4jU2Sy2vdZRCGn/f7vnPJ5SRVezMVW9AiUqEIQhs3pU13iuCm6EZBQsE/oPtsxYXuBBG37oog7mpREKUVXYhY1EBBodZaY9qcXM7v/L55XZy0ZmA2w1zeeWa0uPLtFeNzrtVJUtgWTpKwzcQEmDaIkqQadu4UiXw1YS+5VgtkG4H+L54UgrHNvuki2wymihLhcF1KjhoCJYmSJ54TlJzIaTJdEjXg1RcOM67B+ROP8fh8T6NREwWQZG01LTtNYBtPgvRKYqaXEdBGMNPPunB6geOHZ/jmt39JEiVJbDfVp55+lBePP0LOQljDUeX66jo/3FynVxIlibbiy9/9yWunj9DvZiJMPnr2rZX7W2O9vrigN888qfvbYw36hWcWZlk+e5S5qcJXN+7SKYnhdqu7G402m6q1YaM2rGIbSYxbszZsePujH6lhxmEuvfwUF5eO8en3t/n11pCfb23QyYnV25vkJHISSdLkUBKdnNg/1+XgfJdBP/PFT39TwxzZ16ONYKqbsU2/kykTwhQAGyQImzv3RtQwTRuceXY/OYk/1nYoebIziIffIU0aSLuUe5n333gOG+amO5x4Ypb3Pl9l9a9NprqFMEje82CQ2GMGmjbYGVcGU5mmDb7+ZQ3bJD3ImDB74MVMGnZyZrsJLn1yg3FblSQ+XD7JB8sneeXda7Q1SEo2Yo+ACUQJRYSwdWDQ0aH5PrP9zDufrXJwrseFUwusb43JCYEFsStAJIdt45yTOyW5Wm7aYLpXuHlnk8vXb3Hx/DEODLqMWlskQ7KNbTsp5aSEt0Yt/wwbHEaICJjuFj7+8ndG4+Cl5w+xudOye3UMVspJiyvXrkTUc70S7pWsjZ1qHA/h1mrmpgtJ4t52RJJlsHKW0NX/APMLWxC1Oj8zAAAAAElFTkSuQmCC">AI写作助手</A>
<DT><A HREF="http://ebuymed.cn/freedown/index.html" ADD_DATE="1576410776">免费下载方法_百度文库免费下载方法</A>
<DT><A HREF="https://www.cnblogs.com/cookiewu/p/9845472.html" ADD_DATE="1582466548">将一个word文档按一页或多页拆分成多个文档 - cookiewu - 博客园</A>
<DT><A HREF="https://tool.chinaz.com/tools/unixtime.aspx" ADD_DATE="1596344619" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAh0lEQVQ4jZWS2w2AIAwA2+JCJhoXcCKcwzVcAjeAxlFcwNcHRkmFCPcH3KWQgEobKEJpcwY453aLu0Wx71HaUBgzc322z7Ia5u8AStkpqMi+g3z7DoS9oP16zOyfROKAmiNqd9P6Tsi3AaBKeVE7ciWBsP+DkG3sCwJv5waPnRWENgBg6fe+AHuLWhmoRSQ7AAAAAElFTkSuQmCC">时间戳</A>
<DT><A HREF="https://translatesubtitles.com/subtitletranslator/index.php" ADD_DATE="1596372949" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC3UlEQVQ4jX2TQWgUVxjH/997szVZJ0KT4lqyTtxulrh2goHqpSZuQNCA4kGSFBF6MIJagtBayKWQ0VNBlELa6MEc2mMCDbWDHg3Ek4T1oC4oJBOLCLt0u4tsOjOZee/rwV0JrfZd3sf3vt//Pfj/n8T/rJGRkYOWZZHneY33zYh39IiZCcCHg4ODi/a+fd8DYMdx3jUL+e8GMwsi4kuTk7PlSuVwIpH41Orufj5769bjsbExWSqV+L0CTVhPTU19Z5rmN7+7bhxsbsrh4eEjgvnhHdddm5+flwsLC/wfgRZ8xXGczq6uK78uLioppajVahwrlTxx8uQJ0zSfTk9PP3McRywtLTEAUBMmIhLXr137IW1Zk67rqiAIKJFICCJCo9FQ+XxeHjxw4O+79+59NTc393OTYaNZ4KeZmR8/P3TowkqxGA8NDQnDMITWGkTERCR931dMlJyYmLhtmiYT0S/MTAYR8flz577cPzBwoVypxLtSKSGlFMwMIuLmC1kIIcMgUEopWSgUZorF4goRlQwAH/hBcHH25k29sbGBrXDTzlbNRCTiOI67Ojt3fJxKnQXwrdHb27u7/vp1tlqtUstCAFBKQUrJDEArBSEEiAhaa2o0GtyxffsAABgcBETM0vd9Zn7jThRFOp/PyyiKkEwmUa/Xsb6+rtvb2iiKY0gpmTo6JACI1ZcvXxiG8cSyLBGGodLM3G/bsm3bNj8IAv1XtbqR2rkzymazYjOKtJQSmUxGbIbhg1YOtNK69EkmczSbzXZa6TSFYbj0qFhcANGg7/u1tdXVq325XLanp+ej3em0qNdq9++47mUA/tYgdtu2/UUulzsOIHnm9Onf+vv71eFCQY+Ojl4GsMO27VO9e/YcA9D29uNs2d/Gc3x8/Ou9fX03PM+DaZpItrfj4crKZ8vLy8UtwWMAMFpJbopIAOx53qs/K5XbRPSH1jqhtd5VLpdV85yIKG5d9g+2U13JIPOGogAAAABJRU5ErkJggg==">Subtitles translator V2</A>
<DT><A HREF="http://htmlpreview.github.io/" ADD_DATE="1597506224">GitHub &amp; BitBucket HTML Preview</A>
<DT><A HREF="https://acrobatusers.com/actions-exchange/" ADD_DATE="1598099387" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAA90lEQVQ4jZWRoZKDMBRFz+4gHo7ISGTrqKOST2g/ob/R36nE8gnIyEZGUtc4nqxYlllC6cxGJZlz7n2ZfDnn+M/KgKqqkluNEZCi+HsZYwwhfL/Pud3YaN4QYuRwSOI/CiL0/ZreFooC79f0tpDnOBdVE/qNMEEhsN/TdYgkQJb2itB1WpacTlyvqFLXqKJKWU7ColcV5zif6Tqahr6XtlVjqGueT4zJ0unbFmsRYbfDWpomDoN4T4w8HkvBe+53Qpgm+S0UY/R4nI4hZPOOtgW4XGZaZ239aER+BlBrecctBFXFmClbFRjHcSbyPE+FYRg+RCZ/9wLdEn9HCxva0gAAAABJRU5ErkJggg==">Acrobat Actions Exchange - Adobe Acrobat</A>
<DT><A HREF="https://www.digitalocean.com/community/tools/nginx" ADD_DATE="1598102429" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACNUlEQVQ4jX3Tv4teRRTG8c+Z9+7u+8YExBQWi4VgIa6VLhpd1MVi/4MFCxFBEVGMSFCxUC5KUgQkxYIgRmvhLWxFRJeAhRAElQVFGxGVVbJCor6/7r3HYq9xbXymOXMeZubMnO8EkEEkeDUfUDyFDdyMxL70meKiOi4dXRP+0Ut5wjHnhCeFoQ7/uodxmknv+cvLzse1Pp2hdkIaG9ky0akU0FpIoVL189bQwNRHrti2E1dLX/o5I1tmZipF61OtbXOnhHstPKKxa2BgamZoy03OHlbwem7ofCIMFAOtC/a8aByto9rOgTVvGnhep5UaPFjpPGtgSUiNj9XOEGkzK5s6sKsYR0OesWZd5X5pReOJCg8j+vEWkbZzYByN3evnd32udXteVNmQUjhVdKZaP5v5wdS3h+1BnUWd5foWa7KPvtPodEJarRT3mAup870DIo21xv5fIZGVOn79j1HnMa27hUoxwWV1NPZ6KsIdKkUnpZ8qr+RJK1bN/WbZvrnbLPlQZaTxo7l123lgHK0XcqR4ur9/4FKx5FHHfWnZaXV0ioUwUgkMrfjTOFrP5HE3etvAXTqd1jWtdyrpioU9pDrv1LkVn5tbkQ4U96lzVXpOsa4xN7Js4oI34uuwmZVd6TWn3eC8ia/wkD0Ta26RLlt2UotOGgoT7zvwuB3zYldHHNpU/beZ9yQ2Qulxorhq6qxfPGYnZkRWRNe/7gemvsHv9hxivBCW/KGz3+P+rjq+ONq0vwHGVepcT9t+ZgAAAABJRU5ErkJggg==">NGINX Config | DigitalOcean</A>
<DT><A HREF="https://tableconvert.com/?output=latex" ADD_DATE="1602117751" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACt0lEQVQ4jZWSP2idZRjFz3ne97vfvbdtDB06OJRM3kYRodilYm2QDgrSKV0EB6FKp9I26OjnWE2Ik2CKi4JIOqioCFK5SSkOrpKYSoYKKvTPVL259/u+932OQ5IuTj3L8wzn4eHwOwSAma+qaU4dfMLSxNEFOCq0/eq7f2JfVWWoKp+9tXimdfy1fWphE6oMrJxPrS2eiGarqtNhEg7B0SsiqGubL1xewLCKmKvS02sfXoZ4GmVx34FPt05e/Bmr88GMPG6dOEP4FI3TgA6b2RScpwEY5qo0+OmDC9bvLjHa0TRJXwTwndn1xVM4dz2b5I2Su8QslwNIcheBCQAfrC+9Gcvi4/xw3JB8rnOws6y6+c3K8sLszeXjEQBAPBra2yUBAEII8ywCsNPIx01rITwL4yTXzbrn/JJR6JA0QBRgchgEguwCYGrTJW/THXaLEgDyw506HOqfsGBH/x1tf2IObijlB4ihYeCYgRMGq0n8AgC/zy1spTa/gmh3rF8WYfpAmUbjLzdvfPP636+t7BAABj9efRL98hAnOwKA0O/6xq9bf+DtlRar8wHnrufBrauDouh9rrbd2Ljx7Xm8t5bxfkU8pv53wGPD5ZnQsY8oPyJ5Fijrdswn7WebL15aAYBjN5fOx175huq2IWACIoz3U9teiWA6Y+WBsz4ag8GA7CAJEF0A1wAokG+RfF7ZgT2P9Xpg0/4QBSSN66w6OYyU5GITQO0A0C5SjDRusuqUYTS5JKtNQNrrAY0kxN3nMO6i3M9tJEijUSKMpEAaXDTCotwpySlIDsldgOKjbsmj3CWXKEiSy520EKKIu4hB7KEACLoH63fhdXNvPwIsPLBux9xlMAOhADNJ+W68Pfznu2denjrrno/ImWCA6ta8GQ/3UWXTRU3arx1ypAyaooB7t4dXvv8PY9Rw3xJIiyoAAAAASUVORK5CYII=">Convert Table to LaTex Table - Table Convert Online</A>
"""

soup = bs(html, 'lxml')

# lst = soup.find_all(class_="codelist codelist-desktop cate1")
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
with open('1.txt', 'w', encoding='utf-8') as f:
    for item in lst:
        url = item['href']
        img_url = "https://www.google.com/s2/favicons?domain=" + item['href'].split('/')[2]
        title = item.text
        text = item.text
        f.write(string.format(url, url, img_url, title, text))


head_div = """  
<h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id="{}"></i>{}</h4>
<div class="row">
"""

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
