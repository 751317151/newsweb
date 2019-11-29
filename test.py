'''
@Author: 华豪
@Date: 2019-11-25 17:37:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-29 19:23:44
'''

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

    variety_features_news_title = data1.xpath('//*[@id="hot-clicks"]/ol/li/a/text()')
    variety_features_news_url = data1.xpath('//*[@id="hot-clicks"]/ol/li/a/@href')
    for i in range(len(variety_features_news_title)):
        print(variety_features_news_title[i],variety_features_news_url[i])
        # cur.execute('insert into entertainment_entertainment values (default,"%s","%s","variety_features_news",0)'%(variety_features_news_title[i],variety_features_news_url[i]))
        # conn.commit()

    
    
    


