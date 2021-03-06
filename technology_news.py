'''
@Author: 华豪
@Date: 2019-11-27 17:27:28
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-17 15:11:56
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/tech'
}

def top_news():
    url = "https://news.baidu.com/tech"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    # 图片新闻
    pop1 = data.index('cpOptions_1.data.push')
    data2 = data[pop1:]
    # print(data2)
    titles = list(filter(lambda x:'"title"' in x,data2.split('\n')))
    urls = list(filter(lambda x:'"url"' in x,data2.split('\n')))
    imgurls = list(filter(lambda x:"imgUrl" in x,data2.split('\n')))
    abs_titles = list(filter(lambda x:"abs" in x,data2.split('\n')))
    try:
        cur.execute('delete from technology_technology where abs_titles="tupian"')
        for i in range(len(titles)):
            title = titles[i].strip()[:-1].split(":")[-1]
            abs_title = abs_titles[i].strip().split(":")[-1]
            url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
            imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

            print(title)
            print(url)
            print(abs_title)
            print(imgurl)
            cur.execute('insert into technology_technology values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
        conn.commit()
    except:
        conn.rollback()
    
    internet_news_title = data1.xpath('//*[@id="internet_news"]//a/text()')
    internet_news_url = data1.xpath('//*[@id="internet_news"]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="internet_news"')
        for i in range(len(internet_news_title)):
            print(internet_news_title[i],internet_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","internet_news",0)'%(internet_news_title[i],internet_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    middle_news_title = data1.xpath('//*[@id="col_focus"]/div[2]/div//a/text()')
    middle_news_url = data1.xpath('//*[@id="col_focus"]/div[2]/div//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="middle_news"')
        for i in range(len(middle_news_title)):
            print(middle_news_title[i],middle_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","middle_news",0)'%(middle_news_title[i],middle_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    science_news_title = data1.xpath('//*[@id="kj_news"]//a/text()')
    science_news_url = data1.xpath('//*[@id="kj_news"]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="science_news"')
        for i in range(len(science_news_title)):
            print(science_news_title[i],science_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","science_news",0)'%(science_news_title[i],science_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    technology_video_news_title = data1.xpath('//*[@id="kj_video"]/div//a/span/text()')
    technology_video_news_url = data1.xpath('//*[@id="kj_video"]/div//a/@href')
    technology_video_news_imgurl = data1.xpath('//*[@id="kj_video"]/div//a/img/@src')
    try:
        cur.execute('delete from technology_technology where abs_titles="technology_video_news"')
        for i in range(len(technology_video_news_title)):
            print(technology_video_news_title[i],technology_video_news_url[i],technology_video_news_imgurl[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","technology_video_news","%s")'%(technology_video_news_title[i],technology_video_news_url[i],technology_video_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()
    
    technology_news_title = data1.xpath('//*[@id="kj_video"]/ul//a/text()')
    technology_news_url = data1.xpath('//*[@id="kj_video"]/ul//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="technology_news"')
        for i in range(len(technology_news_title)):
            print(technology_news_title[i],technology_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","technology_news",0)'%(technology_news_title[i],technology_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def yejie_news():
    url = "http://news.baidu.com/widget?id=Industry&channel=tech"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    communication_news_title = data1.xpath('//*[@id="tongxin_news"]/div[2]/ul//a/text()')
    communication_news_url = data1.xpath('//*[@id="tongxin_news"]/div[2]/ul//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="communication_news"')
        for i in range(len(communication_news_title)):
            print(communication_news_title[i],communication_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","communication_news",0)'%(communication_news_title[i],communication_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

    middle_focus_news_title = data1.xpath('//*[@id="col_yejie"]/div[3]/div//a/text()')
    middle_focus_news_url = data1.xpath('//*[@id="col_yejie"]/div[3]/div//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="middle_focus_news"')
        for i in range(len(middle_focus_news_title)):
            print(middle_focus_news_title[i],middle_focus_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","middle_focus_news",0)'%(middle_focus_news_title[i],middle_focus_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    company_news_title = data1.xpath('//*[@id="rwgs_news_list"]//a/text()')
    company_news_url = data1.xpath('//*[@id="rwgs_news_list"]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="company_news"')
        for i in range(len(company_news_title)):
            print(company_news_title[i],company_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","company_news",0)'%(company_news_title[i],company_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def shouji_news():
    url = "https://news.baidu.com/tech"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    iphone_news_title = data1.xpath('//*[@id="cell_iphone"]/div[2]//a/text()')
    iphone_news_url = data1.xpath('//*[@id="cell_iphone"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="iphone_news"')
        for i in range(len(iphone_news_title)):
            print(iphone_news_title[i],iphone_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","iphone_news",0)'%(iphone_news_title[i],iphone_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    android_news_title = data1.xpath('//*[@id="cell_news"]/div[2]//a/text()')
    android_news_url = data1.xpath('//*[@id="cell_news"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="android_news"')
        for i in range(len(android_news_title)):
            print(android_news_title[i],android_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","android_news",0)'%(android_news_title[i],android_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    shouji_middle_news_title = data1.xpath('//*[@id="col_shouji"]/div[3]/div//a/text()')
    shouji_middle_news_url = data1.xpath('//*[@id="col_shouji"]/div[3]/div//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="shouji_middle_news"')
        for i in range(len(shouji_middle_news_title)):
            print(shouji_middle_news_title[i],shouji_middle_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","shouji_middle_news",0)'%(shouji_middle_news_title[i],shouji_middle_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    shouji_right_news_title = data1.xpath('//*[@id="new_cell"]/div[2]//a/text()')
    shouji_right_news_url = data1.xpath('//*[@id="new_cell"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="shouji_right_news"')
        for i in range(len(shouji_right_news_title)):
            print(shouji_right_news_title[i],shouji_right_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","shouji_right_news",0)'%(shouji_right_news_title[i],shouji_right_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def shuma_news():
    url = "https://news.baidu.com/tech"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    panel_computer_news_title = data1.xpath('//*[@id="sm_pbdn"]/div[2]//a/text()')
    panel_computer_news_url = data1.xpath('//*[@id="sm_pbdn"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="panel_computer_news"')
        for i in range(len(panel_computer_news_title)):
            print(panel_computer_news_title[i],panel_computer_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","panel_computer_news",0)'%(panel_computer_news_title[i],panel_computer_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    E_book_news_title = data1.xpath('//*[@id="sm_ebook"]/div[2]//a/text()')
    E_book_news_url = data1.xpath('//*[@id="sm_ebook"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="E_book_news"')
        for i in range(len(E_book_news_title)):
            print(E_book_news_title[i],E_book_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","E_book_news",0)'%(E_book_news_title[i],E_book_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    shuma_middle_news_title = data1.xpath('//*[@id="col_shuma"]/div[3]/div//a/text()')
    shuma_middle_news_url = data1.xpath('//*[@id="col_shuma"]/div[3]/div//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="shuma_middle_news"')
        for i in range(len(shuma_middle_news_title)):
            print(shuma_middle_news_title[i],shuma_middle_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","shuma_middle_news",0)'%(shuma_middle_news_title[i],shuma_middle_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    new_computer_news_title = data1.xpath('//*[@id="sm_new"]/div[2]//a/text()')
    new_computer_news_url = data1.xpath('//*[@id="sm_new"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="new_computer_news"')
        for i in range(len(new_computer_news_title)):
            print(new_computer_news_title[i],new_computer_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","new_computer_news",0)'%(new_computer_news_title[i],new_computer_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def science_news():
    url = "http://news.baidu.com/widget?id=Science&channel=tech"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    universe_news_title = data1.xpath('//*[@id="kx_yzts"]/div[2]//a/text()')
    universe_news_url = data1.xpath('//*[@id="kx_yzts"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="universe_news"')
        for i in range(len(universe_news_title)):
            print(universe_news_title[i],universe_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","universe_news",0)'%(universe_news_title[i],universe_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    history_news_title = data1.xpath('//*[@id="kx_lskg"]/div[2]//a/text()')
    history_news_url = data1.xpath('//*[@id="kx_lskg"]/div[2]//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="history_news"')
        for i in range(len(history_news_title)):
            print(history_news_title[i],history_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","history_news",0)'%(history_news_title[i],history_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    science_middle_news_title = data1.xpath('//*[@id="col_kexue"]/div[3]/div//a/text()')
    science_middle_news_url = data1.xpath('//*[@id="col_kexue"]/div[3]/div//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="science_middle_news"')
        for i in range(len(science_middle_news_title)):
            print(science_middle_news_title[i],science_middle_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","science_middle_news",0)'%(science_middle_news_title[i],science_middle_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    science_discovery_video_news_title = data1.xpath('//*[@id="kxts_video"]/div//a/span/text()')
    science_discovery_video_news_url = data1.xpath('//*[@id="kxts_video"]/div//a/@href')
    science_discovery_video_news_imgurl = data1.xpath('//*[@id="kxts_video"]/div//a/img/@src')
    try:
        cur.execute('delete from technology_technology where abs_titles="science_discovery_video_news"')
        for i in range(len(science_discovery_video_news_title)):
            print(science_discovery_video_news_title[i],science_discovery_video_news_url[i],science_discovery_video_news_imgurl[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","science_discovery_video_news","%s")'%(science_discovery_video_news_title[i],science_discovery_video_news_url[i],science_discovery_video_news_imgurl[i]))
        conn.commit()
    except:
        conn.rollback()
    
    science_discovery_news_title = data1.xpath('//*[@id="kxts_video"]/ul//a/text()')
    science_discovery_news_url = data1.xpath('//*[@id="kxts_video"]/ul//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="science_discovery_news"')
        for i in range(len(science_discovery_news_title)):
            print(science_discovery_news_title[i],science_discovery_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","science_discovery_news",0)'%(science_discovery_news_title[i],science_discovery_news_url[i]))
        conn.commit()
    except:
        conn.rollback()
    
    hot_click_news_title = data1.xpath('//*[@id="hot_tophit"]/div[2]/ul//a/text()')
    hot_click_news_url = data1.xpath('//*[@id="hot_tophit"]/div[2]/ul//a/@href')
    try:
        cur.execute('delete from technology_technology where abs_titles="hot_click_news"')
        for i in range(len(hot_click_news_title)):
            print(hot_click_news_title[i],hot_click_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","hot_click_news",0)'%(hot_click_news_title[i],hot_click_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=tech'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')
    try:
        cur.execute('delete from technology_technology where abs_titles="latest_news"')
        for i in range(len(latest_news_url)):
            print(latest_news_title[i],latest_news_url[i])
            cur.execute('insert into technology_technology values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
        conn.commit()
    except:
        conn.rollback()

if __name__ == '__main__':
    try:
        top_news()
        yejie_news()
        shouji_news()
        shuma_news()
        science_news()
        latest_news()
    except:
        print("出错")
