'''
@Author: 华豪
@Date: 2019-10-24 11:34:26
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-12 14:32:54
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()


# 热点新闻
def top_news():
    url = "https://news.baidu.com/sports"
    # 基本新闻
    data = requests.get(url).text
    data1 = etree.HTML(data)

    top_sports_news_url = data1.xpath('//*[@id="col_focus"]/div[1]//a/@href')
    top_sports_news_title = data1.xpath('//*[@id="col_focus"]/div[1]//a/text()')

    for i in range(20):
        print(top_sports_news_url[i],top_sports_news_title[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s",0,0)'%(top_sports_news_title[i],top_sports_news_url[i]))
        # conn.commit()

    # 四张图片新闻
    pop1 = data.index('cpOptions_1.data.push')
    data2 = data[pop1:]
    # print(data2)
    titles = list(filter(lambda x:"title" in x,data2.split('\n')))
    urls = list(filter(lambda x:'"url"' in x,data2.split('\n')))
    imgurls = list(filter(lambda x:"imgUrl" in x,data2.split('\n')))
    abs_titles = list(filter(lambda x:"abs" in x,data2.split('\n')))

    for i in range(len(titles)):
        title = titles[i].strip()[:-1].split(":")[-1]
        abs_title = abs_titles[i].strip().split(":")[-1]
        url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
        imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

        print(title)
        print(url)
        print(abs_title)
        print(imgurl)
        # cur.execute('insert into sports_sports values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
        # conn.commit()
    
    NBA_news_url = data1.xpath('//*[@id="col_nba"]/div[1]/div[2]//a/@href')
    NBA_news_title = data1.xpath('//*[@id="col_nba"]/div[1]/div[2]//a/text()')

    for i in range(12):
        print(NBA_news_title[i],NBA_news_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","NBA_news",0)'%(NBA_news_title[i],NBA_news_url[i]))
        # conn.commit()

def world_football():
    url = 'https://news.baidu.com/widget?id=WorldSoccerNews&channel=sports&t=1573377253196'
    data = requests.get(url,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    world_football_url = data1.xpath('//*[@id="col_internal"]/div[1]/div[2]//a/@href')
    world_football_title = data1.xpath('//*[@id="col_internal"]/div[1]/div[2]//a/text()')

    star_news_url = data1.xpath('//*[@id="star-news"]//a/@href')
    star_news_title = data1.xpath('//*[@id="star-news"]//a/text()')

    # print(world_football_url,world_football_title)
    for i in range(12):
        print(world_football_title[i],world_football_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","world_football",0)'%(world_football_title[i],world_football_url[i]))
        # conn.commit()
    
    for i in range(8):
        print(star_news_title[i],star_news_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","star_news",0)'%(star_news_title[i],star_news_url[i]))
        # conn.commit()

def china_football():
    url = 'http://news.baidu.com/widget?id=ChinaSoccerNews&channel=sports&t=1573456554645'
    data = requests.get(url,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    china_football_url = data1.xpath('//*[@id="col_civil"]/div[1]/div[2]//a/@href')
    china_football_title = data1.xpath('//*[@id="col_civil"]/div[1]/div[2]//a/text()')

    player_news_url = data1.xpath('//*[@id="player-trends"]//a/@href')
    player_news_title = data1.xpath('//*[@id="player-trends"]//a/text()')

    # print(world_football_url,world_football_title)
    for i in range(12):
        print(china_football_title[i],china_football_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","china_football",0)'%(china_football_title[i],china_football_url[i]))
        # conn.commit()
    
    for i in range(8):
        print(player_news_title[i],player_news_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","player_news",0)'%(player_news_title[i],player_news_url[i]))
        # conn.commit()

def CBA():
    url = 'http://news.baidu.com/widget?id=CbaNews&channel=sports&t=1573459692944'
    data = requests.get(url,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    CBA_news_url = data1.xpath('//*[@id="col_cba"]/div[1]/div[2]//a/@href')
    CBA_news_title = data1.xpath('//*[@id="col_cba"]/div[1]/div[2]//a/text()')

    focus_events_url = data1.xpath('//*[@id="focus-events"]//a/@href')
    focus_events_title = data1.xpath('//*[@id="focus-events"]//a/text()')

    # print(world_football_url,world_football_title)
    for i in range(12):
        print(CBA_news_title[i],CBA_news_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","CBA_news",0)'%(CBA_news_title[i],CBA_news_url[i]))
        # conn.commit()
    
    for i in range(8):
        print(focus_events_title[i],focus_events_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","focus_events",0)'%(focus_events_title[i],focus_events_url[i]))
        # conn.commit()

def other_sports():
    url = 'http://news.baidu.com/widget?id=OtherNews&channel=sports&t=1573459692963'
    data = requests.get(url,verify=False).text
    data1 = etree.HTML(data)
    # print(data)
    other_sports_url = data1.xpath('//*[@id="col_integrated"]/div[1]/div[2]//a/@href')
    other_sports_title = data1.xpath('//*[@id="col_integrated"]/div[1]/div[2]//a/text()')

    hot_articles_url = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/@href')
    hot_articles_title = data1.xpath('//*[@id="hot-article"]/ul/li//a[1]/text()')

    # print(world_football_url,world_football_title)
    for i in range(12):
        print(other_sports_title[i],other_sports_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","other_sports",0)'%(other_sports_title[i],other_sports_url[i]))
        # conn.commit()
    
    for i in range(8):
        print(hot_articles_title[i],hot_articles_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","hot_articles",0)'%(hot_articles_title[i],hot_articles_url[i]))
        # conn.commit()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=sports&t=1573462748116'
    data = requests.get(url,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')

    for i in range(len(latest_news_url)):
        print(latest_news_title[i],latest_news_url[i])
        # cur.execute('insert into sports_sports values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
        # conn.commit()

if __name__ == '__main__':
    # top_news()
    # world_football()
    # china_football()
    # CBA()
    # other_sports()
    latest_news()
