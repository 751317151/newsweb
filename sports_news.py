'''
@Author: 华豪
@Date: 2019-10-24 11:34:26
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-17 15:07:39
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/sports'
}

# 热点新闻
def top_news():
    url = "https://news.baidu.com/sports"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    top_sports_news_url = data1.xpath('//*[@id="col_focus"]/div[1]//a/@href')
    top_sports_news_title = data1.xpath('//*[@id="col_focus"]/div[1]//a/text()')
    try:
        cur.execute('delete from sports_sports where abs_titles="top_sports_news"')
        for i in range(20):
            print(top_sports_news_url[i],top_sports_news_title[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","top_sports_news",0)'%(top_sports_news_title[i],top_sports_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

    # 四张图片新闻
    pop1 = data.index('cpOptions_1.data.push')
    data2 = data[pop1:]
    # print(data2)
    titles = list(filter(lambda x:"title" in x,data2.split('\n')))
    urls = list(filter(lambda x:'"url"' in x,data2.split('\n')))
    imgurls = list(filter(lambda x:"imgUrl" in x,data2.split('\n')))
    abs_titles = list(filter(lambda x:"abs" in x,data2.split('\n')))
    try:
        cur.execute('delete from sports_sports where abs_titles="tupian"')
        for i in range(len(titles)):
            title = titles[i].strip()[:-1].split(":")[-1]
            abs_title = abs_titles[i].strip().split(":")[-1]
            url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
            imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

            print(title)
            print(url)
            print(abs_title)
            print(imgurl)
            cur.execute('insert into sports_sports values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
        conn.commit()
    except:
        conn.rollback()
    
    NBA_news_url = data1.xpath('//*[@id="col_nba"]/div[1]/div[2]//a/@href')
    NBA_news_title = data1.xpath('//*[@id="col_nba"]/div[1]/div[2]//a/text()')
    try:
        cur.execute('delete from sports_sports where abs_titles="NBA_news"')
        for i in range(12):
            print(NBA_news_title[i],NBA_news_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","NBA_news",0)'%(NBA_news_title[i],NBA_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

    video_news_imgurl = data1.xpath('//*[@id="sports-videos"]//img/@src')
    video_news_title = data1.xpath('//*[@id="sports-videos"]/div/p[2]/a/text()')
    video_news_url = data1.xpath('//*[@id="sports-videos"]/div/p[2]/a/@href')
    try:
        cur.execute('delete from sports_sports where abs_titles="video_news"')
        for i in range(len(video_news_title)):
            print(video_news_title[i],video_news_url[i],video_news_imgurl[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","video_news","%s")'%(video_news_title[i],video_news_url[i],video_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()

def world_football():
    url = 'https://news.baidu.com/widget?id=WorldSoccerNews&channel=sports&t=1573377253196'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    world_football_url = data1.xpath('//*[@id="col_internal"]/div[1]/div[2]//a/@href')
    world_football_title = data1.xpath('//*[@id="col_internal"]/div[1]/div[2]//a/text()')

    star_news_url = data1.xpath('//*[@id="star-news"]//a/@href')
    star_news_title = data1.xpath('//*[@id="star-news"]//a/text()')
    try:
        cur.execute('delete from sports_sports where abs_titles="world_football"')
        for i in range(12):
            print(world_football_title[i],world_football_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","world_football",0)'%(world_football_title[i],world_football_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    try:
        cur.execute('delete from sports_sports where abs_titles="star_news"')
        for i in range(8):
            print(star_news_title[i],star_news_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","star_news",0)'%(star_news_title[i],star_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def china_football():
    url = 'http://news.baidu.com/widget?id=ChinaSoccerNews&channel=sports&t=1573456554645'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    china_football_url = data1.xpath('//*[@id="col_civil"]/div[1]/div[2]//a/@href')
    china_football_title = data1.xpath('//*[@id="col_civil"]/div[1]/div[2]//a/text()')

    player_news_url = data1.xpath('//*[@id="player-trends"]//a/@href')
    player_news_title = data1.xpath('//*[@id="player-trends"]//a/text()')

    try:
        cur.execute('delete from sports_sports where abs_titles="china_football"')
        for i in range(12):
            print(china_football_title[i],china_football_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","china_football",0)'%(china_football_title[i],china_football_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    try:
        cur.execute('delete from sports_sports where abs_titles="player_news"')
        for i in range(8):
            print(player_news_title[i],player_news_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","player_news",0)'%(player_news_title[i],player_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def CBA():
    url = 'http://news.baidu.com/widget?id=CbaNews&channel=sports&t=1573459692944'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    CBA_news_url = data1.xpath('//*[@id="col_cba"]/div[1]/div[2]//a/@href')
    CBA_news_title = data1.xpath('//*[@id="col_cba"]/div[1]/div[2]//a/text()')

    focus_events_url = data1.xpath('//*[@id="focus-events"]//a/@href')
    focus_events_title = data1.xpath('//*[@id="focus-events"]//a/text()')

    try:
        cur.execute('delete from sports_sports where abs_titles="CBA_news"')
        for i in range(12):
            print(CBA_news_title[i],CBA_news_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","CBA_news",0)'%(CBA_news_title[i],CBA_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    try:
        cur.execute('delete from sports_sports where abs_titles="focus_events"')
        for i in range(8):
            print(focus_events_title[i],focus_events_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","focus_events",0)'%(focus_events_title[i],focus_events_url[i]))
        conn.commit()
    except:
        conn.rollback()

def other_sports():
    url = 'http://news.baidu.com/widget?id=OtherNews&channel=sports&t=1573459692963'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    other_sports_url = data1.xpath('//*[@id="col_integrated"]/div[1]/div[2]//a/@href')
    other_sports_title = data1.xpath('//*[@id="col_integrated"]/div[1]/div[2]//a/text()')

    hot_articles_url = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/@href')
    hot_articles_title = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/text()')

    try:
        cur.execute('delete from sports_sports where abs_titles="other_sports"')
        for i in range(12):
            print(other_sports_title[i],other_sports_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","other_sports",0)'%(other_sports_title[i],other_sports_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    try:
        cur.execute('delete from sports_sports where abs_titles="hot_articles"')
        for i in range(8):
            print(hot_articles_title[i],hot_articles_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","hot_articles",0)'%(hot_articles_title[i],hot_articles_url[i]))
        conn.commit()
    except:
        conn.rollback()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=sports&t=1573462748116'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')
    try:
        cur.execute('delete from sports_sports where abs_titles="latest_news"')
        for i in range(len(latest_news_url)):
            print(latest_news_title[i],latest_news_url[i])
            cur.execute('insert into sports_sports values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

if __name__ == '__main__':
    try:
        top_news()
        world_football()
        china_football()
        CBA()
        other_sports()
        latest_news()
    except:
        print("出错")
