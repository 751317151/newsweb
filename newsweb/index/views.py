'''
@Author: 华豪
@Date: 2019-11-12 14:16:16
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-26 17:45:26
'''
from django.shortcuts import render
from index.models import index

# Create your views here.

def index_news(request):
    if request.method == 'GET':
        # 热点
        img_news = index.objects.filter(abs_titles='hot_tupian')
        hot_news = index.objects.filter(abs_titles='hot_news')
        hot_pane_news1 = index.objects.filter(abs_titles='hot_pane_news1')
        hot_pane_news = index.objects.filter(abs_titles='hot_pane_news')
        online_news = index.objects.filter(abs_titles='online_news')
        # 国内
        hot_China_news = index.objects.filter(abs_titles='hot_China_news')
        hot_China_pic_news = index.objects.filter(abs_titles='hot_China_pic_news')
        hot_China_click_news = index.objects.filter(abs_titles='hot_China_click_news')
        # 国际
        hot_world_news = index.objects.filter(abs_titles='hot_world_news')
        hot_world_pic_news = index.objects.filter(abs_titles='hot_world_pic_news')
        hot_world_click_news = index.objects.filter(abs_titles='hot_world_click_news')
        # 娱乐
        hot_enter_news = index.objects.filter(abs_titles='hot_enter_news')
        hot_enter_pic_news = index.objects.filter(abs_titles='hot_enter_pic_news')
        hot_enter_click_news = index.objects.filter(abs_titles='hot_enter_click_news')
        hot_enter_div_pic_news = index.objects.filter(abs_titles='hot_enter_div_pic_news')
        # 体育
        hot_sports_news = index.objects.filter(abs_titles='hot_sports_news')
        hot_sports_pic_news = index.objects.filter(abs_titles='hot_sports_pic_news')
        hot_sports_click_news = index.objects.filter(abs_titles='hot_sports_click_news')
        # 科技
        hot_tech_news = index.objects.filter(abs_titles='hot_tech_news')
        hot_tech_pic_news = index.objects.filter(abs_titles='hot_tech_pic_news')
        hot_tech_topic_pic_news = index.objects.filter(abs_titles='hot_tech_topic_pic_news')
        hot_tech_click_news = index.objects.filter(abs_titles='hot_tech_click_news')
        # 军事
        hot_military_news = index.objects.filter(abs_titles='hot_military_news')
        hot_military_pic_news = index.objects.filter(abs_titles='hot_military_pic_news')
        hot_military_click_news = index.objects.filter(abs_titles='hot_military_click_news')

        # 互联网
        hot_internet_news = index.objects.filter(abs_titles='hot_internet_news')
        hot_internet_pic_news = index.objects.filter(abs_titles='hot_internet_pic_news')
        hot_internet_click_news = index.objects.filter(abs_titles='hot_internet_click_news')

        contex = {
            # 热点
            'img_news':img_news,
            'hot_news':hot_news,
            'hot_pane_news1':hot_pane_news1,
            'hot_pane_news21':hot_pane_news[:6],
            'hot_pane_news22':hot_pane_news[6:12],
            'hot_pane_news23':hot_pane_news[12:18],
            'hot_pane_news24':hot_pane_news[18:24],
            'hot_pane_news25':hot_pane_news[24:],
            'online_news1':online_news[:5],
            'online_news2':online_news[5:10],
            'online_news3':online_news[10:],
            # 国内
            'hot_China_news1':hot_China_news[:6],
            'hot_China_news2':hot_China_news[6:],
            'hot_China_pic_news':hot_China_pic_news,
            'hot_China_click_news':hot_China_click_news,
            # 国际
            'hot_world_news1':hot_world_news[:6],
            'hot_world_news2':hot_world_news[6:],
            'hot_world_pic_news':hot_world_pic_news,
            'hot_world_click_news1':hot_world_click_news[:5],
            'hot_world_click_news2':hot_world_click_news[5:],
            # 娱乐
            'hot_enter_news1':hot_enter_news[:6],
            'hot_enter_news2':hot_enter_news[6:],
            'hot_enter_pic_news':hot_enter_pic_news,
            'hot_enter_click_news':hot_enter_click_news,
            'hot_enter_div_pic_news':hot_enter_div_pic_news,
            # 体育
            'hot_sports_news1':hot_sports_news[:6],
            'hot_sports_news2':hot_sports_news[6:],
            'hot_sports_pic_news':hot_sports_pic_news,
            'hot_sports_click_news':hot_sports_click_news,
            # 科技
            'hot_tech_news1':hot_tech_news[:6],
            'hot_tech_news2':hot_tech_news[6:],
            'hot_tech_pic_news':hot_tech_pic_news,
            'hot_tech_topic_pic_news':hot_tech_topic_pic_news,
            'hot_tech_click_news':hot_tech_click_news,
            # 军事
            'hot_military_news1':hot_military_news[:6],
            'hot_military_news2':hot_military_news[6:],
            'hot_military_pic_news':hot_military_pic_news,
            'hot_military_click_news1':hot_military_click_news[:5],
            'hot_military_click_news2':hot_military_click_news[5:],
            # 互联网
            'hot_internet_news1':hot_internet_news[:6],
            'hot_internet_news2':hot_internet_news[6:],
            'hot_internet_pic_news':hot_internet_pic_news,
            'hot_internet_click_news1':hot_internet_click_news[:4],
            'hot_internet_click_news2':hot_internet_click_news[4:],
        }

        return render(request,"index.html",contex)
