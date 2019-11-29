'''
@Author: 华豪
@Date: 2019-11-27 17:27:28
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-29 19:34:18
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

def top_news():
    url = "https://news.baidu.com/ent"
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

    for i in range(len(titles)):
        title = titles[i].strip()[:-1].split(":")[-1]
        abs_title = abs_titles[i].strip().split(":")[-1]
        url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
        imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

        print(title)
        print(url)
        print(abs_title)
        print(imgurl)
        # cur.execute('insert into entertainment_entertainment values (default,%s,"%s","tupian","%s")'%(title,url,imgurl))
        # conn.commit()
    
    instant_news_title = data1.xpath('//*[@id="instant-news"]/ul//a/text()')
    instant_news_url = data1.xpath('//*[@id="instant-news"]/ul//a/@href')
    for i in range(len(instant_news_title)):
        print(instant_news_title[i],instant_news_url[i])
        # instant_news_title[i] = instant_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","instant_news",0)'%(instant_news_title[i],instant_news_url[i]))
        # conn.commit()

def focal_news():
    url = "https://news.baidu.com/ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    focal_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/text()')
    focal_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[2]//a/@href')
    for i in range(len(focal_news_title)):
        print(focal_news_title[i],focal_news_url[i])
        # focal_news_title[i] = focal_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","focal_news",0)'%(focal_news_title[i],focal_news_url[i]))
        # conn.commit()
    
    focal_pic_news_title = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/span/text()')
    focal_pic_news_url = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/@href')
    focal_pic_news_imgurl = data1.xpath('//*[@id="col_focus"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(focal_pic_news_title)):
        print(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","focal_pic_news","%s")'%(focal_pic_news_title[i],focal_pic_news_url[i],focal_pic_news_imgurl[i]))
        # conn.commit()

def star_news():
    url = "http://news.baidu.com/widget?id=Star&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    star_news_title = data1.xpath('//*[@id="col_star"]/div[1]/div[2]//a/text()')
    star_news_url = data1.xpath('//*[@id="col_star"]/div[1]/div[2]//a/@href')
    for i in range(len(star_news_title)):
        print(star_news_title[i],star_news_url[i])
        # star_news_title[i] = star_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","star_news",0)'%(star_news_title[i],star_news_url[i]))
        # conn.commit()
    
    star_pic_news_title = data1.xpath('//*[@id="col_star"]/div[1]/div[3]/ul//a/span/text()')
    star_pic_news_url = data1.xpath('//*[@id="col_star"]/div[1]/div[3]/ul//a/@href')
    star_pic_news_imgurl = data1.xpath('//*[@id="col_star"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(star_pic_news_title)):
        print(star_pic_news_title[i],star_pic_news_url[i],star_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","star_pic_news","%s")'%(star_pic_news_title[i],star_pic_news_url[i],star_pic_news_imgurl[i]))
        # conn.commit()

    rumours_news_title = data1.xpath('//*[@id="zongyi_cwbl"]/ul/li/a/text()')
    rumours_news_url = data1.xpath('//*[@id="zongyi_cwbl"]/ul/li/a/@href')
    for i in range(len(rumours_news_title)):
        print(rumours_news_title[i],rumours_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","rumours_news",0)'%(rumours_news_title[i],rumours_news_url[i]))
        # conn.commit()
    
    variety_video_news_imgurl = data1.xpath('//*[@id="zongyi_video"]/div[2]/div/ul/li/a/img/@r_src')
    variety_video_news_title = data1.xpath('//*[@id="zongyi_video"]/div[2]/div/ul/li/a/span/text()')
    variety_video_news_url = data1.xpath('//*[@id="zongyi_video"]/div[2]/div/ul/li/a/@href')
    for i in range(len(variety_video_news_title)):
        print(variety_video_news_title[i],variety_video_news_url[i],variety_video_news_imgurl[i])
        # variety_video_news_title[i] = variety_video_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","variety_video_news","%s")'%(variety_video_news_title[i],variety_video_news_url[i],variety_video_news_imgurl[i]))
        # conn.commit()

def movie_news():
    url = "http://news.baidu.com/widget?id=Movie&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    movie_news_title = data1.xpath('//*[@id="col_film"]/div[1]/div[2]//a/text()')
    movie_news_url = data1.xpath('//*[@id="col_film"]/div[1]/div[2]//a/@href')
    for i in range(len(movie_news_title)):
        print(movie_news_title[i],movie_news_url[i])
        # movie_news_title[i] = movie_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","movie_news",0)'%(movie_news_title[i],movie_news_url[i]))
        # conn.commit()
    
    movie_pic_news_title = data1.xpath('//*[@id="col_film"]/div[1]/div[3]/ul//a/span/text()')
    movie_pic_news_url = data1.xpath('//*[@id="col_film"]/div[1]/div[3]/ul//a/@href')
    movie_pic_news_imgurl = data1.xpath('//*[@id="col_film"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(movie_pic_news_title)):
        print(movie_pic_news_title[i],movie_pic_news_url[i],movie_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","movie_pic_news","%s")'%(movie_pic_news_title[i],movie_pic_news_url[i],movie_pic_news_imgurl[i]))
        # conn.commit()

    movie_features_news_title = data1.xpath('//*[@id="film_huaxu"]/ul/li/a/text()')
    movie_features_news_url = data1.xpath('//*[@id="film_huaxu"]/ul/li/a/@href')
    for i in range(len(movie_features_news_title)):
        print(movie_features_news_title[i],movie_features_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","movie_features_news",0)'%(movie_features_news_title[i],movie_features_news_url[i]))
        # conn.commit()

def TV_news():
    url = "http://news.baidu.com/widget?id=TV&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    TV_news_title = data1.xpath('//*[@id="col_tv"]/div[1]/div[2]//a/text()')
    TV_news_url = data1.xpath('//*[@id="col_tv"]/div[1]/div[2]//a/@href')
    for i in range(len(TV_news_title)):
        print(TV_news_title[i],TV_news_url[i])
        # TV_news_title[i] = TV_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","TV_news",0)'%(TV_news_title[i],TV_news_url[i]))
        # conn.commit()
    
    TV_pic_news_title = data1.xpath('//*[@id="col_tv"]/div[1]/div[3]/ul//a/span/text()')
    TV_pic_news_url = data1.xpath('//*[@id="col_tv"]/div[1]/div[3]/ul//a/@href')
    TV_pic_news_imgurl = data1.xpath('//*[@id="col_tv"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(TV_pic_news_title)):
        print(TV_pic_news_title[i],TV_pic_news_url[i],TV_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","TV_pic_news","%s")'%(TV_pic_news_title[i],TV_pic_news_url[i],TV_pic_news_imgurl[i]))
        # conn.commit()

    hot_tv_news_title = data1.xpath('//*[@id="hotdramas"]/table//a/text()')
    hot_tv_news_url = data1.xpath('//*[@id="hotdramas"]/table//a/@href')
    # print(hot_tv_news_title,hot_tv_news_url)
    for i in range(len(hot_tv_news_title)):
        print(hot_tv_news_title[i],hot_tv_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","hot_tv_news",0)'%(hot_tv_news_title[i],hot_tv_news_url[i]))
        # conn.commit()
    
    hot_tv_comments_news_title = data1.xpath('//*[@id="hot_recommend"]/div[2]/ul//a/text()')
    hot_tv_comments_news_url = data1.xpath('//*[@id="hot_recommend"]/div[2]/ul//a/@href')
    # print(hot_tv_comments_news_title,hot_tv_comments_news_url)
    for i in range(len(hot_tv_comments_news_title)):
        print(hot_tv_comments_news_title[i],hot_tv_comments_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","hot_tv_comments_news",0)'%(hot_tv_comments_news_title[i],hot_tv_comments_news_url[i]))
        # conn.commit()

def music_news():
    url = "http://news.baidu.com/widget?id=Music&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    music_news_title = data1.xpath('//*[@id="col_music"]/div[1]/div[2]//a/text()')
    music_news_url = data1.xpath('//*[@id="col_music"]/div[1]/div[2]//a/@href')
    for i in range(len(music_news_title)):
        print(music_news_title[i],music_news_url[i])
        # music_news_title[i] = music_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","music_news",0)'%(music_news_title[i],music_news_url[i]))
        # conn.commit()
    
    music_pic_news_title = data1.xpath('//*[@id="col_music"]/div[1]/div[3]/ul//a/span/text()')
    music_pic_news_url = data1.xpath('//*[@id="col_music"]/div[1]/div[3]/ul//a/@href')
    music_pic_news_imgurl = data1.xpath('//*[@id="col_music"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(music_pic_news_title)):
        print(music_pic_news_title[i],music_pic_news_url[i],music_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","music_pic_news","%s")'%(music_pic_news_title[i],music_pic_news_url[i],music_pic_news_imgurl[i]))
        # conn.commit()

    top_music_news_title1 = data1.xpath('//*[@id="music_new_song"]/div[2]/div/table//td[2]/a/text()')
    top_music_news_url1 = data1.xpath('//*[@id="music_new_song"]/div[2]/div/table//td[2]/a/@href')
    top_music_news_title2 = data1.xpath('//*[@id="music_new_song"]/div[2]/div/table//td[3]/a/text()')
    top_music_news_url2 = data1.xpath('//*[@id="music_new_song"]/div[2]/div/table//td[3]/a/@href')
    for i in range(len(top_music_news_title1)):
        print(top_music_news_title1[i],top_music_news_url1[i])
        print(top_music_news_title2[i],top_music_news_url2[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","top_music_news1",0)'%(top_music_news_title1[i],top_music_news_url1[i]))
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","top_music_news2",0)'%(top_music_news_title2[i],top_music_news_url2[i]))
        # conn.commit()
    
    china_music_news_title1 = data1.xpath('//*[@id="music_gold_song"]/div[2]/div/table//td[2]/a/text()')
    china_music_news_url1 = data1.xpath('//*[@id="music_gold_song"]/div[2]/div/table//td[2]/a/@href')
    china_music_news_title2 = data1.xpath('//*[@id="music_gold_song"]/div[2]/div/table//td[3]/a/text()')
    china_music_news_url2 = data1.xpath('//*[@id="music_gold_song"]/div[2]/div/table//td[3]/a/@href')
    for i in range(len(china_music_news_title1)):
        print(china_music_news_title1[i],china_music_news_url1[i])
        print(china_music_news_title2[i],china_music_news_url2[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","china_music_news1",0)'%(china_music_news_title1[i],china_music_news_url1[i]))
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","china_music_news2",0)'%(china_music_news_title2[i],china_music_news_url2[i]))
        # conn.commit()

def variety_news():
    url = "http://news.baidu.com/widget?id=Variety&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    variety_news_title = data1.xpath('//*[@id="col_zongyi"]/div[1]/div[2]//a/text()')
    variety_news_url = data1.xpath('//*[@id="col_zongyi"]/div[1]/div[2]//a/@href')
    for i in range(len(variety_news_title)):
        print(variety_news_title[i],variety_news_url[i])
        # variety_news_title[i] = variety_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","variety_news",0)'%(variety_news_title[i],variety_news_url[i]))
        # conn.commit()
    
    variety_pic_news_title = data1.xpath('//*[@id="col_zongyi"]/div[1]/div[3]/ul//a/span/text()')
    variety_pic_news_url = data1.xpath('//*[@id="col_zongyi"]/div[1]/div[3]/ul//a/@href')
    variety_pic_news_imgurl = data1.xpath('//*[@id="col_zongyi"]/div[1]/div[3]/ul//a/img/@r_src')
    for i in range(len(variety_pic_news_title)):
        print(variety_pic_news_title[i],variety_pic_news_url[i],variety_pic_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","variety_pic_news","%s")'%(variety_pic_news_title[i],variety_pic_news_url[i],variety_pic_news_imgurl[i]))
        # conn.commit()

    variety_click_news_title = data1.xpath('//*[@id="hot-clicks"]/ol/li/a/text()')
    variety_click_news_url = data1.xpath('//*[@id="hot-clicks"]/ol/li/a/@href')
    for i in range(len(variety_click_news_title)):
        print(variety_click_news_title[i],variety_click_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","variety_click_news",0)'%(variety_click_news_title[i],variety_click_news_url[i]))
        # conn.commit()

def picture_news():
    url = "http://news.baidu.com/widget?id=Picture&channel=ent"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    picture_news_title = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/span/text()')
    picture_news_url = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/@href')
    picture_news_imgurl = data1.xpath('//*[@id="mil-picnews"]/div/ul//a/img/@r_src')
    for i in range(len(picture_news_title)):
        print(picture_news_title[i],picture_news_url[i],picture_news_imgurl[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","picture_news","%s")'%(picture_news_title[i],picture_news_url[i],picture_news_imgurl[i]))
        # conn.commit()

def latest_news():
    url = 'http://news.baidu.com/widget?id=LatestNews&channel=ent'
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    latest_news_url = data1.xpath('//*[@id="latest-news"]//a/@href')
    latest_news_title = data1.xpath('//*[@id="latest-news"]//a/text()')

    for i in range(len(latest_news_url)):
        print(latest_news_title[i],latest_news_url[i])
        # latest_news_title[i] = latest_news_title[i].replace(" ",",")
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","latest_news",0)'%(latest_news_title[i],latest_news_url[i]))
        # conn.commit()

if __name__ == '__main__':
    # top_news()
    # focal_news()
    # star_news()
    # movie_news()
    # TV_news()
    # music_news()
    # variety_news()
    # picture_news()
    latest_news()
