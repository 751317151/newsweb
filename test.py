'''
@Author: 华豪
@Date: 2019-11-25 17:37:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-01 15:15:52
'''

def international_military_news():
    url = "http://news.baidu.com/widget?id=InternationalMil&channel=mil"
    # 基本新闻
    data = requests.get(url,headers=headers,verify=False).text
    data1 = etree.HTML(data)

    international_military_news_title = data1.xpath('//*[@id="col_guojijq"]/div[2]/div[2]//a/text()')
    international_military_news_url = data1.xpath('//*[@id="col_guojijq"]/div[2]/div[2]//a/@href')
    for i in range(len(international_military_news_title)):
        print(international_military_news_title[i],international_military_news_url[i])
        # international_military_news_title[i] = international_military_news_title[i].replace(" ",",")
        # cur.execute('insert into military_military values (default,"%s","%s","international_military_news",0)'%(international_military_news_title[i],international_military_news_url[i]))
        # conn.commit()
    
    international_military_pic_news_title = data1.xpath('//*[@id="internationalmil"]/div[3]//a/span/text()')
    international_military_pic_news_url = data1.xpath('//*[@id="internationalmil"]/div[3]//a/@href')
    international_military_pic_news_imgurl = data1.xpath('//*[@id="internationalmil"]/div[3]//a/img/@src')
    for i in range(len(international_military_pic_news_title)):
        print(international_military_pic_news_title[i],international_military_pic_news_url[i],international_military_pic_news_imgurl[i])
        # cur.execute('insert into military_military values (default,"%s","%s","international_military_pic_news","%s")'%(international_military_pic_news_title[i],international_military_pic_news_url[i],international_military_pic_news_imgurl[i]))
        # conn.commit()


    
    
    


