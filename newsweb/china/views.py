'''
@Author: 华豪
@Date: 2019-11-27 15:48:22
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-28 17:44:24
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from china.models import china

# Create your views here.
def china_news(request):
    if request.method == "GET":
        # 热点
        img_news = china.objects.filter(abs_titles='tupian')
        instant_news = china.objects.filter(abs_titles='instant_news')
        # 焦点
        focal_news = china.objects.filter(abs_titles='focal_news')
        focal_video_news = china.objects.filter(abs_titles='video_news')
        # 港澳台
        gangaotai_news = china.objects.filter(abs_titles='gangaotai_news')
        gangaotai_pic_news = china.objects.filter(abs_titles='gangaotai_pic_news')
        gangaotai_click_news = china.objects.filter(abs_titles='gangaotai_click_news')
        # 时政
        politics_news = china.objects.filter(abs_titles='politics_news')
        politics_pic_news = china.objects.filter(abs_titles='politics_pic_news')
        politics_click_news = china.objects.filter(abs_titles='politics_click_news')

        # 最新新闻
        latest_news = china.objects.filter(abs_titles='latest_news')

        contex = {
            # 热点
            'img_news':img_news,
            'instant_news':instant_news,
            # 焦点
            'focal_news1':focal_news[:6],
            'focal_news2':focal_news[6:],
            'focal_video_news':focal_video_news,
            # 港澳台
            'gangaotai_news1':gangaotai_news[:5],
            'gangaotai_news2':gangaotai_news[5:],
            'gangaotai_pic_news':gangaotai_pic_news,
            'gangaotai_click_news':gangaotai_click_news,
            # 时政
            'politics_news1':politics_news[:6],
            'politics_news2':politics_news[6:],
            'politics_pic_news':politics_pic_news,
            'politics_click_news':politics_click_news,
            # 最新新闻
            'latest_news1':latest_news[:10],
            'latest_news2':latest_news[10:],
        }
        return render(request,"china.html",contex)