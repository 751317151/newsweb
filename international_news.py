'''
@Author: 华豪
@Date: 2019-11-28 18:05:24
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-17 15:19:19
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/guoji'
}

def top_news():
    url = "https://news.baidu.com/guoji"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    # 图片新闻
    pop1 = data.index('cpOptions_1.data.push')
    data2 = data[pop1:]
    # print(data2)
    titles = list(filter(lambda x:"title" in x,data2.split('\n')))
    urls = list(filter(lambda x:'"url"' in x,data2.split('\n')))
    imgurls = list(filter(lambda x:"imgUrl" in x,data2.split('\n')))
    abs_titles = list(filter(lambda x:"abs" in x,data2.split('\n')))
    try:
        cur.execute('delete from international_international where abs_titles="tupian"')
        for i in range(len(titles)):
            title = titles[i].strip()[:-1].split(":")[-1]
            abs_title = abs_titles[i].strip().split(":")[-1]
            url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
            imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

            print(title)
            print(url)
            print(abs_title)
            print(imgurl)
            cur.execute('insert into international_international values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
        conn.commit()
    except:
        conn.rollback()
    
    instant_news_title = data1.xpath('//*[@id="instant-news"]/ul//a/text()')
    instant_news_url = data1.xpath('//*[@id="instant-news"]/ul//a/@href')
    try:
        cur.execute('delete from international_international where abs_titles="instant_news"')
        for i in range(len(instant_news_title)):
            print(instant_news_title[i],instant_news_url[i])
            # instant_news_title[i] = instant_news_title[i].replace(" ",",")
            cur.execute('insert into international_international values (default,"%s","%s","instant_news",0)'%(instant_news_title[i],instant_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def focal_news():
    url = "https://news.baidu.com/guoji"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    focal_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/text()')
    focal_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/@href')
    try:
        cur.execute('delete from international_international where abs_titles="focal_news"')
        for i in range(len(focal_news_title)):
            print(focal_news_title[i],focal_news_url[i])
            cur.execute('insert into international_international values (default,"%s","%s","focal_news",0)'%(focal_news_title[i],focal_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

    focal_pic_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/span/text()')
    focal_pic_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/@href')
    focal_pic_news_imgurl = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/img/@src')
    try:
        cur.execute('delete from international_international where abs_titles="focal_pic_news"')
        for i in range(len(focal_pic_news_title)):
            print(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i])
            url = focal_pic_news_imgurl[i]
            data = requests.get(url,headers=headers).content
            # print(data)
            focal_pic_news_imgurl[i] = 'focal_pic_news_imgurl%s'%i
            with open('newsweb/static/images/international/'+focal_pic_news_imgurl[i]+'.jpg','wb') as f:
                f.write(data)
            cur.execute('insert into international_international values (default,"%s","%s","focal_pic_news","%s")'%(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()
    
    focal_pictures_news_title = data1.xpath('//*[@id="focus-aside-news"]/div[2]/div/ul//a/span/text()')
    focal_pictures_news_url = data1.xpath('//*[@id="focus-aside-news"]/div[2]/div/ul//a/@href')
    focal_pictures_news_imgurl = data1.xpath('//*[@id="focus-aside-news"]/div[2]/div/ul//a/img/@r_src')
    try:
        cur.execute('delete from international_international where abs_titles="focal_pictures_news"')
        for i in range(len(focal_pictures_news_title)):
            print(focal_pictures_news_title[i],focal_pictures_news_url[i],focal_pictures_news_imgurl[i])
            url = focal_pictures_news_imgurl[i]
            data = requests.get(url,headers=headers).content
            # print(data)
            focal_pictures_news_imgurl[i] = 'focal_pictures_news_imgurl%s'%i
            with open('newsweb/static/images/international/'+focal_pictures_news_imgurl[i]+'.jpg','wb') as f:
                f.write(data)
            cur.execute('insert into international_international values (default,"%s","%s","focal_pictures_news","%s")'%(focal_pictures_news_title[i],focal_pictures_news_url[i],focal_pictures_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()

def military_news():
    url = "http://news.baidu.com/widget?id=MilitaryNews&channel=guoji"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    military_news_title = data1.xpath('//*[@id="MilitaryNews"]/div[2]//a/text()')
    military_news_url = data1.xpath('//*[@id="MilitaryNews"]/div[2]//a/@href')
    try:
        cur.execute('delete from international_international where abs_titles="military_news"')
        for i in range(len(military_news_title)):
            print(military_news_title[i],military_news_url[i])
            cur.execute('insert into international_international values (default,"%s","%s","military_news",0)'%(military_news_title[i],military_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

    military_pic_news_title = data1.xpath('//*[@id="MilitaryNews"]/div[3]//a/span/text()')
    military_pic_news_url = data1.xpath('//*[@id="MilitaryNews"]/div[3]//a/@href')
    military_pic_news_imgurl = data1.xpath('//*[@id="MilitaryNews"]/div[3]//a/img/@src')
    try:
        cur.execute('delete from international_international where abs_titles="military_pic_news"')
        for i in range(len(military_pic_news_title)):
            print(military_pic_news_title[i],military_pic_news_url[i],military_pic_news_imgurl[i])
            url = military_pic_news_imgurl[i]
            data = requests.get(url,headers=headers).content
            # print(data)
            military_pic_news_imgurl[i] = 'military_pic_news_imgurl%s'%i
            with open('newsweb/static/images/international/'+military_pic_news_imgurl[i]+'.jpg','wb') as f:
                f.write(data)
            cur.execute('insert into international_international values (default,"%s","%s","military_pic_news","%s")'%(military_pic_news_title[i],military_pic_news_url[i],military_pic_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()

def hot_news():
    url = "http://news.baidu.com/widget?id=HotNews&channel=guoji"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    hot_news_title = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/text()')
    hot_news_url = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/@href')
    try:
        cur.execute('delete from international_international where abs_titles="hot_news"')
        for i in range(len(hot_news_title)):
            print(hot_news_title[i],hot_news_url[i])
            cur.execute('insert into international_international values (default,"%s","%s","hot_news",0)'%(hot_news_title[i],hot_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=guoji'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')
    try:
        cur.execute('delete from international_international where abs_titles="latest_news"')
        for i in range(len(latest_news_url)):
            print(latest_news_title[i],latest_news_url[i])
            cur.execute('insert into international_international values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

if __name__ == '__main__':
    try:
        top_news()
        focal_news()
        military_news()
        hot_news()
        latest_news()
    except:
        print("出错")
