'''
@Author: 华豪
@Date: 2019-12-01 14:30:10
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-13 21:46:12
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from military.models import military

# Create your views here.
def military_news(request):
    if request.method == "GET":
        # 热点
        img_news = military.objects.filter(abs_titles='tupian')
        instant_news = military.objects.filter(abs_titles='instant_news')
        # 焦点
        focal_news = military.objects.filter(abs_titles='focal_news')
        focal_pic_news = military.objects.filter(abs_titles='focal_pic_news')
        # 视频
        video_news = military.objects.filter(abs_titles='video_news')
        # 中国军情
        china_military_news = military.objects.filter(abs_titles='china_military_news')
        china_military_pic_news = military.objects.filter(abs_titles='china_military_pic_news')
        taiwan_focus_news = military.objects.filter(abs_titles='taiwan_focus_news')
        # 国际
        international_military_news = military.objects.filter(abs_titles='international_military_news')
        international_military_pic_news = military.objects.filter(abs_titles='international_military_pic_news')
        hot_news = military.objects.filter(abs_titles='hot_news')
        # 图片
        military_picture_news = military.objects.filter(abs_titles='military_picture_news')
        # 最新新闻
        latest_news = military.objects.filter(abs_titles='latest_news')

        contex = {
            # 热点
            'img_news':img_news,
            'instant_news':instant_news,
            # 焦点
            'focal_news1':focal_news[:6],
            'focal_news2':focal_news[6:],
            'focal_pic_news':focal_pic_news,
            # 视频
            'video_news':video_news,
            # 中国
            'china_military_news1':china_military_news[:6],
            'china_military_news2':china_military_news[6:],
            'china_military_pic_news':china_military_pic_news,
            'taiwan_focus_news':taiwan_focus_news,
            # 国际
            'international_military_news1':international_military_news[:6],
            'international_military_news2':international_military_news[6:],
            'international_military_pic_news':international_military_pic_news,
            'hot_news':hot_news,
            # 图片
            'military_picture_news':military_picture_news,
            # 最新新闻
            'latest_news1':latest_news[:10],
            'latest_news2':latest_news[10:],
            'username': request.session.get("username"),
        }
        return render(request,"military.html",contex) 
