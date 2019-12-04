'''
@Author: 华豪
@Date: 2019-11-25 17:37:09
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-04 17:14:26
'''
focal_pic_news_url = focal_pic_news_url + focal_pic_news_url1
    focal_pic_news_title = focal_pic_news_title + focal_pic_news_title1
    focal_pic_news_imgurl = focal_pic_news_imgurl + focal_pic_news_imgurl1



url = focal_pic_news_imgurl[i]
        data = requests.get(url,headers=headers).content
        # print(data)
        focal_pic_news_imgurl[i] = 'focal_pic_news_imgurl%s'%i
        with open('newsweb/static/images/entertainment/'+focal_pic_news_imgurl[i]+'.jpg','wb') as f:
            f.write(data)
    
    
    


