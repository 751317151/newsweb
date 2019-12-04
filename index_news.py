'''
@Author: 华豪
@Date: 2019-11-12 14:32:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-04 15:52:20
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'referer': 'http://news.baidu.com/'
}

# 热搜
def hot_news():
    url = "http://news.baidu.com/"

    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)
    # print(data)

    # 热搜新闻词
    hot_news_url = data1.xpath('//div[@id="news-hotwords"]/div[2]//a/@href')
    hot_news_title = data1.xpath('//div[@id="news-hotwords"]/div[2]//a/@title')
    cur.execute('delete from index_index where abs_titles="hot_news"')
    for i in range(len(hot_news_url)):
        print(hot_news_url[i],hot_news_title[i],len(hot_news_url[i]))
        cur.execute('insert into index_index values (default,"%s","%s","hot_news",0)'%(hot_news_title[i],hot_news_url[i]))
    conn.commit()

    # 图片新闻
    pop1 = data.index('cpOptions_1.data.push')
    data2 = data[pop1:]
    # print(data2)
    titles = list(filter(lambda x:'"title"' in x,data2.split('\n')))
    urls = list(filter(lambda x:'"url"' in x,data2.split('\n')))
    imgurls = list(filter(lambda x:"imgUrl" in x,data2.split('\n')))
    abs_titles = list(filter(lambda x:"abs" in x,data2.split('\n')))

    cur.execute('delete from index_index where abs_titles="hot_tupian"')
    for i in range(len(titles)//2):
        title = titles[i*2].strip()[:-1].split(":")[-1]
        abs_title = abs_titles[i].strip().split(":")[-1]
        url = "http:////" + urls[2*i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]
        imgurl = "http:////" + imgurls[i].strip()[:-1].split(":")[-1].replace('\\','').strip('\/\/')[:-1]

        print(title)
        print(url)
        print(abs_title)
        print(imgurl)
        cur.execute('insert into index_index values (default,%s,"%s","hot_tupian","%s")'%(title,url,imgurl))
    conn.commit()

    # 热点要闻
    hot_pane_news_url = data1.xpath('//*[@id="pane-news"]/ul/li/a[1]/@href')
    hot_pane_news_title = data1.xpath('//*[@id="pane-news"]/ul/li/a[1]/text()')

    cur.execute('delete from index_index where abs_titles="hot_pane_news"')
    # print(hot_pane_news_title,hot_pane_news_url)
    for i in range(len(hot_pane_news_url)):
        print(hot_pane_news_title[i],hot_pane_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_pane_news',0)"%(hot_pane_news_title[i],hot_pane_news_url[i]))
    conn.commit()

    # 时事在线
    online_news_url = data1.xpath('//*[@id="baijia"]/div[3]/div/ul/li/a/@href')
    online_news_title = data1.xpath('//*[@id="baijia"]/div[3]/div/ul/li/a/text()')
    
    cur.execute('delete from index_index where abs_titles="online_news"')
    for i in range(len(online_news_url)):
        print(online_news_title[i],online_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','online_news',0)"%(online_news_title[i],online_news_url[i]))
    conn.commit()

def hot_pane_news():
    url = "http://www.china.com/"

    data = requests.get(url,headers=headers,verify=False)
    data.encoding="utf-8"
    data = data.text
    # print(data)
    data1 = etree.HTML(data)

    # 热点要闻
    hot_pane_news_url = data1.xpath('//*[@id="spotlight"]/div/div[1]//ul//li//a[1]/@href')
    hot_pane_news_title = data1.xpath('//*[@id="spotlight"]/div/div[1]//ul//li//a[1]/text()')
    
    cur.execute('delete from index_index where abs_titles="hot_pane_news1"')
    for i in range(5):
        print(hot_pane_news_title[i],hot_pane_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_pane_news1',0)"%(hot_pane_news_title[i],hot_pane_news_url[i]))
    conn.commit()

def hot_China_news():
    url = "http://news.baidu.com/widget?id=civilnews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_China_news_url = data1.xpath('//*[@id="guonei"]/div[2]//a/@href')
    hot_China_news_title = data1.xpath('//*[@id="guonei"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_China_news"')
    for i in range(len(hot_China_news_url)):
        print(hot_China_news_title[i],hot_China_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_China_news',0)"%(hot_China_news_title[i],hot_China_news_url[i]))
    conn.commit()

    hot_China_pic_news_url = data1.xpath('//*[@id="guonei"]/div[3]/div/div[2]/div//a//@href')
    hot_China_pic_news_title = data1.xpath('//*[@id="guonei"]/div[3]/div/div[2]/div//a//text()')
    hot_China_pic_news_imgurl = data1.xpath('//*[@id="guonei"]/div[3]/div/div[2]/div//a//img/@src')

    hot_China_pic_news_url1 = data1.xpath('//*[@id="guonei"]/div[4]/div/div[2]/div//a//@href')
    hot_China_pic_news_title1 = data1.xpath('//*[@id="guonei"]/div[4]/div/div[2]/div//a//text()')
    hot_China_pic_news_imgurl1 = data1.xpath('//*[@id="guonei"]/div[4]/div/div[2]/div//a//img/@src')

    hot_China_pic_news_url = hot_China_pic_news_url + hot_China_pic_news_url1
    hot_China_pic_news_title = hot_China_pic_news_title + hot_China_pic_news_title1
    hot_China_pic_news_imgurl = hot_China_pic_news_imgurl + hot_China_pic_news_imgurl1
    cur.execute('delete from index_index where abs_titles="hot_China_pic_news"')
    for i in range(len(hot_China_pic_news_imgurl)):
        print(hot_China_pic_news_title[i],hot_China_pic_news_url[i*2],hot_China_pic_news_imgurl[i])
        url = hot_China_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_China_pic_news_imgurl[i] = 'hot_China_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_China_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_China_pic_news','%s')"%(hot_China_pic_news_title[i],hot_China_pic_news_url[i*2],hot_China_pic_news_imgurl[i]))
    conn.commit()

    hot_China_click_news_title = data1.xpath('//*[@id="civil-aside-tophit"]/div[2]/ol//a/text()')
    hot_China_click_news_url = data1.xpath('//*[@id="civil-aside-tophit"]/div[2]/ol//a/@href')
    cur.execute('delete from index_index where abs_titles="hot_China_click_news"')
    for i in range(len(hot_China_click_news_title)):
        print(hot_China_click_news_title[i],hot_China_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_China_click_news',0)"%(hot_China_click_news_title[i],hot_China_click_news_url[i]))
    conn.commit()

def hot_world_news():
    url = "http://news.baidu.com/widget?id=InternationalNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)

    hot_world_news_url = data1.xpath('//*[@id="guojie"]/div[2]//a/@href')
    hot_world_news_title = data1.xpath('//*[@id="guojie"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_world_news"')
    for i in range(len(hot_world_news_url)):
        print(hot_world_news_title[i],hot_world_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_world_news',0)"%(hot_world_news_title[i],hot_world_news_url[i]))
    conn.commit()

    hot_world_pic_news_url = data1.xpath('//*[@id="guojie"]/div[3]/div/div[2]/div//a//@href')
    hot_world_pic_news_title = data1.xpath('//*[@id="guojie"]/div[3]/div/div[2]/div//a//text()')
    hot_world_pic_news_imgurl = data1.xpath('//*[@id="guojie"]/div[3]/div/div[2]/div//a//img/@src')

    hot_world_pic_news_url1 = data1.xpath('//*[@id="guojie"]/div[4]/div/div[2]/div//a//@href')
    hot_world_pic_news_title1 = data1.xpath('//*[@id="guojie"]/div[4]/div/div[2]/div//a//text()')
    hot_world_pic_news_imgurl1 = data1.xpath('//*[@id="guojie"]/div[4]/div/div[2]/div//a//img/@src')
    
    hot_world_pic_news_url = hot_world_pic_news_url + hot_world_pic_news_url1
    hot_world_pic_news_title = hot_world_pic_news_title + hot_world_pic_news_title1
    hot_world_pic_news_imgurl = hot_world_pic_news_imgurl + hot_world_pic_news_imgurl1
    cur.execute('delete from index_index where abs_titles="hot_world_pic_news"')
    for i in range(len(hot_world_pic_news_imgurl)):
        print(hot_world_pic_news_title[i],hot_world_pic_news_url[i*2],hot_world_pic_news_imgurl[i])
        url = hot_world_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_world_pic_news_imgurl[i] = 'hot_world_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_world_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_world_pic_news','%s')"%(hot_world_pic_news_title[i],hot_world_pic_news_url[i*2],hot_world_pic_news_imgurl[i]))
    conn.commit()

    hot_world_click_news_url = data1.xpath('//*[@id="internal-hotword"]/div[2]//a/@href')
    hot_world_click_news_title = data1.xpath('//*[@id="internal-hotword"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_world_click_news"')
    for i in range(len(hot_world_click_news_title)):
        print(hot_world_click_news_title[i],hot_world_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_world_click_news',0)"%(hot_world_click_news_title[i],hot_world_click_news_url[i]))
    conn.commit()

def hot_enter_news():
    url = "http://news.baidu.com/widget?id=EnterNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)

    hot_enter_news_url = data1.xpath('//*[@id="yule"]/div[2]//a/@href')
    hot_enter_news_title = data1.xpath('//*[@id="yule"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_enter_news"')
    for i in range(len(hot_enter_news_url)):
        print(hot_enter_news_title[i],hot_enter_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_enter_news',0)"%(hot_enter_news_title[i],hot_enter_news_url[i]))
    conn.commit()

    hot_enter_pic_news_url = data1.xpath('//*[@id="yule"]/div[3]/div/div[2]/div//a//@href')
    hot_enter_pic_news_title = data1.xpath('//*[@id="yule"]/div[3]/div/div[2]/div//a//text()')
    hot_enter_pic_news_imgurl = data1.xpath('//*[@id="yule"]/div[3]/div/div[2]/div//a//img/@src')

    hot_enter_pic_news_url1 = data1.xpath('//*[@id="yule"]/div[4]/div/div[2]/div//a//@href')
    hot_enter_pic_news_title1 = data1.xpath('//*[@id="yule"]/div[4]/div/div[2]/div//a//text()')
    hot_enter_pic_news_imgurl1 = data1.xpath('//*[@id="yule"]/div[4]/div/div[2]/div//a//img/@src')
    
    hot_enter_pic_news_url = hot_enter_pic_news_url + hot_enter_pic_news_url1
    hot_enter_pic_news_title = hot_enter_pic_news_title + hot_enter_pic_news_title1
    hot_enter_pic_news_imgurl = hot_enter_pic_news_imgurl + hot_enter_pic_news_imgurl1
    cur.execute('delete from index_index where abs_titles="hot_enter_pic_news"')
    for i in range(len(hot_enter_pic_news_imgurl)):
        print(hot_enter_pic_news_title[i],hot_enter_pic_news_url[i*2],hot_enter_pic_news_imgurl[i])
        url = hot_enter_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_enter_pic_news_imgurl[i] = 'hot_enter_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_enter_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_enter_pic_news','%s')"%(hot_enter_pic_news_title[i],hot_enter_pic_news_url[i*2],hot_enter_pic_news_imgurl[i]))
    conn.commit()

    hot_enter_click_news_url = data1.xpath('//*[@id="yule-aside-hotwords"]/div/ul//a/@href')
    hot_enter_click_news_title = data1.xpath('//*[@id="yule-aside-hotwords"]/div/ul//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_enter_click_news"')
    for i in range(len(hot_enter_click_news_url)):
        print(hot_enter_click_news_title[i],hot_enter_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_enter_click_news',0)"%(hot_enter_click_news_title[i],hot_enter_click_news_url[i]))
    conn.commit()
    
    hot_enter_div_pic_news_url = data1.xpath('//*[@id="sports-picwall"]/div/div/div//a//@href')
    hot_enter_div_pic_news_title = data1.xpath('//*[@id="sports-picwall"]/div/div/div//a//text()')
    hot_enter_div_pic_news_imgurl = data1.xpath('//*[@id="sports-picwall"]/div/div/div//a//@src')
    cur.execute('delete from index_index where abs_titles="hot_enter_div_pic_news"')
    for i in range(len(hot_enter_div_pic_news_imgurl)):
        print(hot_enter_div_pic_news_title[i],hot_enter_div_pic_news_url[i*2],hot_enter_div_pic_news_imgurl[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_enter_div_pic_news','%s')"%(hot_enter_div_pic_news_title[i],hot_enter_div_pic_news_url[i*2],hot_enter_div_pic_news_imgurl[i]))
    conn.commit()

def hot_sports_news():
    url = "http://news.baidu.com/widget?id=SportNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_sports_news_url = data1.xpath('//*[@id="tiyu"]/div[2]//a/@href')
    hot_sports_news_title = data1.xpath('//*[@id="tiyu"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_sports_news"')
    for i in range(len(hot_sports_news_url)):
        print(hot_sports_news_title[i],hot_sports_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_sports_news',0)"%(hot_sports_news_title[i],hot_sports_news_url[i]))
    conn.commit()

    hot_sports_pic_news_url = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//@href')
    hot_sports_pic_news_title = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//text()')
    hot_sports_pic_news_imgurl = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//img/@src')

    hot_sports_pic_news_url1 = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//@href')
    hot_sports_pic_news_title1 = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//text()')
    hot_sports_pic_news_imgurl1 = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//img/@src')

    hot_sports_pic_news_url = hot_sports_pic_news_url + hot_sports_pic_news_url1
    hot_sports_pic_news_title = hot_sports_pic_news_title + hot_sports_pic_news_title1
    hot_sports_pic_news_imgurl = hot_sports_pic_news_imgurl + hot_sports_pic_news_imgurl1
    cur.execute('delete from index_index where abs_titles="hot_sports_pic_news"')    
    for i in range(len(hot_sports_pic_news_imgurl)):
        print(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i])
        url = hot_sports_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_sports_pic_news_imgurl[i] = 'hot_sports_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_sports_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_sports_pic_news','%s')"%(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i]))
    conn.commit()

    hot_sports_click_news_title = data1.xpath('//*[@id="sports-aside-cell"]/div[2]/ul//a/text()')
    hot_sports_click_news_url = data1.xpath('//*[@id="sports-aside-cell"]/div[2]/ul//a/@href')
    cur.execute('delete from index_index where abs_titles="hot_sports_click_news"')
    for i in range(len(hot_sports_click_news_title)):
        print(hot_sports_click_news_title[i],hot_sports_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_sports_click_news',0)"%(hot_sports_click_news_title[i],hot_sports_click_news_url[i]))
    conn.commit()

def hot_tech_news():
    url = "http://news.baidu.com/widget?id=TechNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_tech_news_url = data1.xpath('//*[@id="col-tech"]/div[2]//a/@href')
    hot_tech_news_title = data1.xpath('//*[@id="col-tech"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_tech_news"')
    for i in range(len(hot_tech_news_url)):
        print(hot_tech_news_title[i],hot_tech_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_tech_news',0)"%(hot_tech_news_title[i],hot_tech_news_url[i]))
    conn.commit()

    hot_tech_pic_news_url = data1.xpath('//*[@id="col-tech"]/div[3]/div/div[2]/div//a//@href')
    hot_tech_pic_news_title = data1.xpath('//*[@id="col-tech"]/div[3]/div/div[2]/div//a//text()')
    hot_tech_pic_news_imgurl = data1.xpath('//*[@id="col-tech"]/div[3]/div/div[2]/div//a//img/@src')
    cur.execute('delete from index_index where abs_titles="hot_tech_pic_news"')
    for i in range(len(hot_tech_pic_news_imgurl)):
        print(hot_tech_pic_news_title[i],hot_tech_pic_news_url[i*2],hot_tech_pic_news_imgurl[i])
        url = hot_tech_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_tech_pic_news_imgurl[i] = 'hot_tech_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_tech_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_tech_pic_news','%s')"%(hot_tech_pic_news_title[i],hot_tech_pic_news_url[i*2],hot_tech_pic_news_imgurl[i]))
    conn.commit()

    hot_tech_topic_pic_news_url = data1.xpath('//*[@id="tech-aside-cell"]/div[2]/div/div[1]/a/@href')
    hot_tech_topic_pic_news_title = data1.xpath('//*[@id="tech-aside-cell"]/div[2]/div/div[2]/h4/a/text()')
    hot_tech_topic_pic_news_imgurl = data1.xpath('//*[@id="tech-aside-cell"]/div[2]/div/div[1]/a/img/@src')
    cur.execute('delete from index_index where abs_titles="hot_tech_topic_pic_news"')
    for i in range(len(hot_tech_topic_pic_news_url)):
        print(hot_tech_topic_pic_news_title[i],hot_tech_topic_pic_news_url[i],hot_tech_topic_pic_news_imgurl[i])
        url = hot_tech_topic_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_tech_topic_pic_news_imgurl[i] = 'hot_tech_topic_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_tech_topic_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_tech_topic_pic_news','%s')"%(hot_tech_topic_pic_news_title[i],hot_tech_topic_pic_news_url[i],hot_tech_topic_pic_news_imgurl[i]))
    conn.commit()
    
    hot_tech_click_news_title = data1.xpath('//*[@id="tech-aside-zrdl"]/div/ul//a/text()')
    hot_tech_click_news_url = data1.xpath('//*[@id="tech-aside-zrdl"]/div/ul//a/@href')
    cur.execute('delete from index_index where abs_titles="hot_tech_click_news"')
    for i in range(len(hot_tech_click_news_title)):
        print(hot_tech_click_news_title[i],hot_tech_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_tech_click_news',0)"%(hot_tech_click_news_title[i],hot_tech_click_news_url[i]))
    conn.commit()

def hot_military_news():
    url = "http://news.baidu.com/widget?id=MilitaryNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_military_news_url = data1.xpath('//*[@id="junshi"]/div[2]//a/@href')
    hot_military_news_title = data1.xpath('//*[@id="junshi"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_military_news"')
    for i in range(len(hot_military_news_url)):
        print(hot_military_news_title[i],hot_military_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_military_news',0)"%(hot_military_news_title[i],hot_military_news_url[i]))
    conn.commit()

    hot_military_pic_news_url = data1.xpath('//*[@id="junshi"]/div[3]/div/div[2]/div//a//@href')
    hot_military_pic_news_title = data1.xpath('//*[@id="junshi"]/div[3]/div/div[2]/div//a//text()')
    hot_military_pic_news_imgurl = data1.xpath('//*[@id="junshi"]/div[3]/div/div[2]/div//a//img/@src')
    cur.execute('delete from index_index where abs_titles="hot_military_pic_news"')
    for i in range(len(hot_military_pic_news_imgurl)):
        print(hot_military_pic_news_title[i],hot_military_pic_news_url[i*2],hot_military_pic_news_imgurl[i])
        url = hot_military_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_military_pic_news_imgurl[i] = 'hot_military_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_military_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_military_pic_news','%s')"%(hot_military_pic_news_title[i],hot_military_pic_news_url[i*2],hot_military_pic_news_imgurl[i]))
    conn.commit()
    
    hot_military_click_news_title = data1.xpath('//*[@id="junshi"]/div[4]//a/text()')
    hot_military_click_news_url = data1.xpath('//*[@id="junshi"]/div[4]//a/@href')
    cur.execute('delete from index_index where abs_titles="hot_military_click_news"')
    for i in range(len(hot_military_click_news_url)):
        print(hot_military_click_news_title[i],hot_military_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_military_click_news',0)"%(hot_military_click_news_title[i],hot_military_click_news_url[i]))
    conn.commit()

def hot_internet_news():
    url = "http://news.baidu.com/widget?id=InternetNews"

    data = requests.get(url,headers=headers,verify=False).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_internet_news_url = data1.xpath('//*[@id="hulianwang"]/div[2]//a/@href')
    hot_internet_news_title = data1.xpath('//*[@id="hulianwang"]/div[2]//a/text()')
    cur.execute('delete from index_index where abs_titles="hot_internet_news"')
    for i in range(len(hot_internet_news_url)):
        print(hot_internet_news_title[i],hot_internet_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_internet_news',0)"%(hot_internet_news_title[i],hot_internet_news_url[i]))
    conn.commit()

    hot_internet_pic_news_url = data1.xpath('//*[@id="hulianwang"]/div[3]/div/div[2]/div//a//@href')
    hot_internet_pic_news_title = data1.xpath('//*[@id="hulianwang"]/div[3]/div/div[2]/div//a//text()')
    hot_internet_pic_news_imgurl = data1.xpath('//*[@id="hulianwang"]/div[3]/div/div[2]/div//a//img/@src')
    cur.execute('delete from index_index where abs_titles="hot_internet_pic_news"')
    for i in range(len(hot_internet_pic_news_imgurl)):
        print(hot_internet_pic_news_title[i],hot_internet_pic_news_url[i*2],hot_internet_pic_news_imgurl[i])
        url = hot_internet_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        hot_internet_pic_news_imgurl[i] = 'hot_internet_pic_news_imgurl%s'%i
        with open('newsweb/static/images/index/'+hot_internet_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
        cur.execute("insert into index_index values (default,'%s','%s','hot_internet_pic_news','%s')"%(hot_internet_pic_news_title[i],hot_internet_pic_news_url[i*2],hot_internet_pic_news_imgurl[i]))
    conn.commit()
    
    hot_internet_click_news_title = data1.xpath('//*[@id="hulianwang"]/div[4]//a/text()')
    hot_internet_click_news_url = data1.xpath('//*[@id="hulianwang"]/div[4]//a/@href')
    cur.execute('delete from index_index where abs_titles="hot_internet_click_news"')
    for i in range(len(hot_internet_click_news_url)):
        print(hot_internet_click_news_title[i],hot_internet_click_news_url[i])
        cur.execute("insert into index_index values (default,'%s','%s','hot_internet_click_news',0)"%(hot_internet_click_news_title[i],hot_internet_click_news_url[i]))
    conn.commit()

if __name__ == '__main__':
    try:
        hot_news()
        hot_pane_news()
        hot_China_news()
        hot_world_news()
        hot_enter_news()
        hot_sports_news()
        hot_tech_news()
        hot_military_news()
        hot_internet_news()
    except:
        print("出错")
    
