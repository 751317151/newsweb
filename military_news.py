'''
@Author: 华豪
@Date: 2019-11-27 17:27:28
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-04 16:57:12
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/military'
}

def top_news():
    url = "https://news.baidu.com/mil"
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

    cur.execute('delete from military_military where abs_titles="tupian"')
    for i in range(len(titles)):
        title = titles[i].strip()[:-1].split(":")[-1]
        abs_title = abs_titles[i].strip().split(":")[-1]
        url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
        imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

        print(title)
        print(url)
        print(abs_title)
        print(imgurl)
        cur.execute('insert into military_military values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
    conn.commit()
    
    instant_news_title = data1.xpath('//*[@id="instant-news"]/ul//a/text()')
    instant_news_url = data1.xpath('//*[@id="instant-news"]/ul//a/@href')
    cur.execute('delete from military_military where abs_titles="instant_news"')
    for i in range(len(instant_news_title)):
        print(instant_news_title[i],instant_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","instant_news",0)'%(instant_news_title[i],instant_news_url[i]))
    conn.commit()

def focal_news():
    url = "https://news.baidu.com/mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    focal_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/text()')
    focal_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/@href')
    cur.execute('delete from military_military where abs_titles="focal_news"')
    for i in range(len(focal_news_title)):
        print(focal_news_title[i],focal_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","focal_news",0)'%(focal_news_title[i],focal_news_url[i]))
    conn.commit()
    
    focal_pic_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/span/text()')
    focal_pic_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/@href')
    focal_pic_news_imgurl = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/img/@src')
    cur.execute('delete from military_military where abs_titles="focal_pic_news"')
    for i in range(len(focal_pic_news_title)):
        print(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i])
        url = focal_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        focal_pic_news_imgurl[i] = 'focal_pic_news_imgurl%s'%i
        with open('newsweb/static/images/military/'+focal_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into military_military values (default,"%s","%s","focal_pic_news","%s")'%(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i]))
    conn.commit()

    video_news_imgurl = data1.xpath('//*[@id="mil-video"]//img/@src')
    video_news_title = data1.xpath('//*[@id="mil-video"]/div/p[2]/a/text()')
    video_news_url = data1.xpath('//*[@id="mil-video"]/div/p[2]/a/@href')
    cur.execute('delete from military_military where abs_titles="video_news"')
    for i in range(len(video_news_title)):
        print(video_news_title[i],video_news_url[i],video_news_imgurl[i])
        cur.execute('insert into military_military values (default,"%s","%s","video_news","%s")'%(video_news_title[i],video_news_url[i],video_news_imgurl[i]))
    conn.commit()

def china_military_news():
    url = "http://news.baidu.com/widget?id=ChinaMil&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    china_military_news_title = data1.xpath('//*[@id="Chinamil"]/div[2]//a/text()')
    china_military_news_url = data1.xpath('//*[@id="Chinamil"]/div[2]//a/@href')
    cur.execute('delete from military_military where abs_titles="china_military_news"')
    for i in range(len(china_military_news_title)):
        print(china_military_news_title[i],china_military_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","china_military_news",0)'%(china_military_news_title[i],china_military_news_url[i]))
    conn.commit()
    
    china_military_pic_news_title = data1.xpath('//*[@id="Chinamil"]/div[3]//a/span/text()')
    china_military_pic_news_url = data1.xpath('//*[@id="Chinamil"]/div[3]//a/@href')
    china_military_pic_news_imgurl = data1.xpath('//*[@id="Chinamil"]/div[3]//a/img/@src')
    cur.execute('delete from military_military where abs_titles="china_military_pic_news"')
    for i in range(len(china_military_pic_news_title)):
        print(china_military_pic_news_title[i],china_military_pic_news_url[i],china_military_pic_news_imgurl[i])
        url = china_military_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        china_military_pic_news_imgurl[i] = 'china_military_pic_news_imgurl%s'%i
        with open('newsweb/static/images/military/'+china_military_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into military_military values (default,"%s","%s","china_military_pic_news","%s")'%(china_military_pic_news_title[i],china_military_pic_news_url[i],china_military_pic_news_imgurl[i]))
    conn.commit()

def taiwan_focus_news():
    url = "http://news.baidu.com/widget?id=TaiwanFoucs&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    taiwan_focus_news_title = data1.xpath('//*[@id="thjj-news"]//a/text()')
    taiwan_focus_news_url = data1.xpath('//*[@id="thjj-news"]//a/@href')
    cur.execute('delete from military_military where abs_titles="taiwan_focus_news"')
    for i in range(len(taiwan_focus_news_title)):
        print(taiwan_focus_news_title[i],taiwan_focus_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","taiwan_focus_news",0)'%(taiwan_focus_news_title[i],taiwan_focus_news_url[i]))
    conn.commit()

def international_military_news():
    url = "http://news.baidu.com/widget?id=InternationalMil&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    international_military_news_title = data1.xpath('/html/body/div/div[2]//a/text()')
    international_military_news_url = data1.xpath('/html/body/div/div[2]//a/@href')
    cur.execute('delete from military_military where abs_titles="international_military_news"')
    for i in range(len(international_military_news_title)):
        print(international_military_news_title[i],international_military_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","international_military_news",0)'%(international_military_news_title[i],international_military_news_url[i]))
    conn.commit()
    
    international_military_pic_news_title = data1.xpath('/html/body/div/div[3]//a/span/text()')
    international_military_pic_news_url = data1.xpath('/html/body/div/div[3]//a/@href')
    international_military_pic_news_imgurl = data1.xpath('/html/body/div/div[3]//a/img/@src')
    cur.execute('delete from military_military where abs_titles="international_military_pic_news"')
    for i in range(len(international_military_pic_news_title)):
        print(international_military_pic_news_title[i],international_military_pic_news_url[i],international_military_pic_news_imgurl[i])
        url = international_military_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        international_military_pic_news_imgurl[i] = 'international_military_pic_news_imgurl%s'%i
        with open('newsweb/static/images/military/'+international_military_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into military_military values (default,"%s","%s","international_military_pic_news","%s")'%(international_military_pic_news_title[i],international_military_pic_news_url[i],international_military_pic_news_imgurl[i]))
    conn.commit()

def hot_news():
    url = "http://news.baidu.com/widget?id=HotNews&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    hot_news_title = data1.xpath('//*[@id="hot-article"]//a[1]/text()')
    hot_news_url = data1.xpath('//*[@id="hot-article"]//a[1]/@href')
    cur.execute('delete from military_military where abs_titles="hot_news"')
    for i in range(len(hot_news_title)):
        print(hot_news_title[i],hot_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","hot_news",0)'%(hot_news_title[i],hot_news_url[i]))
    conn.commit()

def military_picture_news():
    url = "http://news.baidu.com/widget?id=MilPic&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    military_picture_news_title = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/span/text()')
    military_picture_news_url = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/@href')
    military_picture_news_imgurl = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/img/@r_src')
    cur.execute('delete from military_military where abs_titles="military_picture_news"')
    for i in range(len(military_picture_news_title)):
        print(military_picture_news_title[i],military_picture_news_url[i],military_picture_news_imgurl[i])
        url = military_picture_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        military_picture_news_imgurl[i] = 'military_picture_news_imgurl%s'%i
        with open('newsweb/static/images/military/'+military_picture_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into military_military values (default,"%s","%s","military_picture_news","%s")'%(military_picture_news_title[i],military_picture_news_url[i],military_picture_news_imgurl[i]))
    conn.commit()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=mil'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')
    cur.execute('delete from military_military where abs_titles="latest_news"')
    for i in range(len(latest_news_url)):
        print(latest_news_title[i],latest_news_url[i])
        cur.execute('insert into military_military values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
    conn.commit()

if __name__ == '__main__':
    try:
        top_news()
        focal_news()
        china_military_news()
        taiwan_focus_news()
        international_military_news()
        hot_news()
        military_picture_news()
        latest_news()
    except:
        print("出错")
