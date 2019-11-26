'''
@Author: 华豪
@Date: 2019-11-25 17:37:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-26 15:18:21
'''
def hot_sports_news():
    url = "http://news.baidu.com/widget?id=SportNews"

    data = requests.get(url,headers=headers).text
    # print(data)
    data1 = etree.HTML(data)
    # print(data)
    hot_sports_news_url = data1.xpath('//*[@id="tiyu"]/div[2]//a/@href')
    hot_sports_news_title = data1.xpath('//*[@id="tiyu"]/div[2]//a/text()')

    # for i in range(len(hot_sports_news_url)):
    #     print(hot_sports_news_title[i],hot_sports_news_url[i])
    #     cur.execute("insert into index_index values (default,'%s','%s','hot_sports_news',0)"%(hot_sports_news_title[i],hot_sports_news_url[i]))
    #     conn.commit()

    hot_sports_pic_news_url = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//@href')
    hot_sports_pic_news_title = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//text()')
    hot_sports_pic_news_imgurl = data1.xpath('//*[@id="tiyu"]/div[3]/div/div[2]/div//a//img/@src')

    for i in range(len(hot_sports_pic_news_imgurl)):
        print(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i])
    #     cur.execute("insert into index_index values (default,'%s','%s','hot_sports_pic_news','%s')"%(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i]))
    #     conn.commit()

    hot_sports_pic_news_url = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//@href')
    hot_sports_pic_news_title = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//text()')
    hot_sports_pic_news_imgurl = data1.xpath('//*[@id="tiyu"]/div[4]/div/div[2]/div//a//img/@src')

    for i in range(len(hot_sports_pic_news_imgurl)):
        print(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i])
    #     cur.execute("insert into index_index values (default,'%s','%s','hot_sports_pic_news','%s')"%(hot_sports_pic_news_title[i],hot_sports_pic_news_url[i*2],hot_sports_pic_news_imgurl[i]))
    #     conn.commit()

    hot_sports_click_news_title = data1.xpath('//*[@id="civil-aside-tophit"]/div[2]/ol//a/text()')
    hot_sports_click_news_url = data1.xpath('//*[@id="civil-aside-tophit"]/div[2]/ol//a/@href')

    # for i in range(len(hot_sports_click_news_title)):
    #     print(hot_sports_click_news_title[i],hot_sports_click_news_url[i])
    #     cur.execute("insert into index_index values (default,'%s','%s','hot_sports_click_news',0)"%(hot_sports_click_news_title[i],hot_sports_click_news_url[i]))
    #     conn.commit()
