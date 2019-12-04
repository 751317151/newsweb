'''
@Author: 华豪
@Date: 2019-11-27 17:27:28
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-04 16:27:03
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/guonei'
}

def top_news():
    url = "https://news.baidu.com/guonei"
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
    cur.execute('delete from china_china where abs_titles="tupian"')
    for i in range(len(titles)):
        title = titles[i].strip()[:-1].split(":")[-1]
        abs_title = abs_titles[i].strip().split(":")[-1]
        url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
        imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

        print(title)
        print(url)
        print(abs_title)
        print(imgurl)
        cur.execute('insert into china_china values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
    conn.commit()
    
    instant_news_title = data1.xpath('//*[@id="instant-news"]/ul//a/text()')
    instant_news_url = data1.xpath('//*[@id="instant-news"]/ul//a/@href')
    cur.execute('delete from china_china where abs_titles="instant_news"')
    for i in range(len(instant_news_title)):
        print(instant_news_title[i],instant_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","instant_news",0)'%(instant_news_title[i],instant_news_url[i]))
    conn.commit()

def focal_news():
    url = "https://news.baidu.com/guonei"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    focal_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/text()')
    focal_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/@href')
    cur.execute('delete from china_china where abs_titles="focal_news"')
    for i in range(len(focal_news_title)):
        print(focal_news_title[i],focal_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","focal_news",0)'%(focal_news_title[i],focal_news_url[i]))
    conn.commit()
    
    # 视频新闻
    video_news_imgurl = data1.xpath('//*[@id="focus-videos"]//img/@src')
    video_news_title = data1.xpath('//*[@id="focus-videos"]/div/p[2]/a/text()')
    video_news_url = data1.xpath('//*[@id="focus-videos"]/div/p[2]/a/@href')
    cur.execute('delete from china_china where abs_titles="video_news"')
    for i in range(len(video_news_title)):
        print(video_news_title[i],video_news_url[i],video_news_imgurl[i])
        cur.execute('insert into china_china values (default,"%s","%s","video_news","%s")'%(video_news_title[i],video_news_url[i],video_news_imgurl[i]))
    conn.commit()

def gangaotai_news():
    url = "http://news.baidu.com/widget?id=GangAoTai&channel=guonei"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    gangaotai_news_title = data1.xpath('//*[@id="col_gangaotai"]/div[1]/div[2]//a/text()')
    gangaotai_news_url = data1.xpath('//*[@id="col_gangaotai"]/div[1]/div[2]//a/@href')
    cur.execute('delete from china_china where abs_titles="gangaotai_news"')
    for i in range(len(gangaotai_news_title)):
        print(gangaotai_news_title[i],gangaotai_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","gangaotai_news",0)'%(gangaotai_news_title[i],gangaotai_news_url[i]))
    conn.commit()
    
    gangaotai_pic_news_title = data1.xpath('//*[@id="col_gangaotai"]/div[1]/div[3]/ul//a/span/text()')
    gangaotai_pic_news_url = data1.xpath('//*[@id="col_gangaotai"]/div[1]/div[3]/ul//a/@href')
    gangaotai_pic_news_imgurl = data1.xpath('//*[@id="col_gangaotai"]/div[1]/div[3]/ul//a/img/@r_src')
    cur.execute('delete from china_china where abs_titles="gangaotai_pic_news"')
    for i in range(len(gangaotai_pic_news_title)):
        print(gangaotai_pic_news_title[i],gangaotai_pic_news_url[i],gangaotai_pic_news_imgurl[i])
        url = gangaotai_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        gangaotai_pic_news_imgurl[i] = 'gangaotai_pic_news_imgurl%s'%i
        with open('newsweb/static/images/china/'+gangaotai_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into china_china values (default,"%s","%s","gangaotai_pic_news","%s")'%(gangaotai_pic_news_title[i],gangaotai_pic_news_url[i],gangaotai_pic_news_imgurl[i]))
    conn.commit()
    
    gangaotai_click_news_title = data1.xpath('//*[@id="twms-news"]/ul//a/text()')
    gangaotai_click_news_url = data1.xpath('//*[@id="twms-news"]/ul//a/@href')
    cur.execute('delete from china_china where abs_titles="gangaotai_click_news"')
    for i in range(len(gangaotai_click_news_title)):
        print(gangaotai_click_news_title[i],gangaotai_click_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","gangaotai_click_news",0)'%(gangaotai_click_news_title[i],gangaotai_click_news_url[i]))
    conn.commit()

def politics_news():
    url = "http://news.baidu.com/widget?id=ShiZheng&channel=guonei"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    politics_news_title = data1.xpath('//*[@id="col_politics"]/div[1]/div[2]//a/text()')
    politics_news_url = data1.xpath('//*[@id="col_politics"]/div[1]/div[2]//a/@href')
    cur.execute('delete from china_china where abs_titles="politics_news"')
    for i in range(len(politics_news_title)):
        print(politics_news_title[i],politics_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","politics_news",0)'%(politics_news_title[i],politics_news_url[i]))
    conn.commit()
    
    politics_pic_news_title = data1.xpath('//*[@id="col_politics"]/div[1]/div[3]/ul//a/span/text()')
    politics_pic_news_url = data1.xpath('//*[@id="col_politics"]/div[1]/div[3]/ul//a/@href')
    politics_pic_news_imgurl = data1.xpath('//*[@id="col_politics"]/div[1]/div[3]/ul//a/img/@r_src')
    cur.execute('delete from china_china where abs_titles="politics_pic_news"')
    for i in range(len(politics_pic_news_title)):
        print(politics_pic_news_title[i],politics_pic_news_url[i],politics_pic_news_imgurl[i])
        url = politics_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        politics_pic_news_imgurl[i] = 'politics_pic_news_imgurl%s'%i
        with open('newsweb/static/images/china/'+politics_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute('insert into china_china values (default,"%s","%s","politics_pic_news","%s")'%(politics_pic_news_title[i],politics_pic_news_url[i],politics_pic_news_imgurl[i]))
    conn.commit()
    
    politics_click_news_title = data1.xpath('//*[@id="historical-news"]/ul//a/text()')
    politics_click_news_url = data1.xpath('//*[@id="historical-news"]/ul//a/@href')
    cur.execute('delete from china_china where abs_titles="politics_click_news"')
    for i in range(len(politics_click_news_title)):
        print(politics_click_news_title[i],politics_click_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","politics_click_news",0)'%(politics_click_news_title[i],politics_click_news_url[i]))
    conn.commit()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=guonei'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')
    cur.execute('delete from china_china where abs_titles="latest_news"')
    for i in range(len(latest_news_url)):
        print(latest_news_title[i],latest_news_url[i])
        cur.execute('insert into china_china values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
    conn.commit()

if __name__ == '__main__':
    try:
        top_news()
        focal_news()
        gangaotai_news()
        politics_news()
        latest_news()
    except:
        print("出错")
