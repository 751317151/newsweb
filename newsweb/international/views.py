'''
@Author: 华豪
@Date: 2019-11-28 17:47:03
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-13 21:45:10
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from international.models import international

# Create your views here.
def international_news(request):
    if request.method == "GET":
        # 热点
        img_news = international.objects.filter(abs_titles='tupian')
        instant_news = international.objects.filter(abs_titles='instant_news')
        # 焦点
        focal_news = international.objects.filter(abs_titles='focal_news')
        focal_pic_news = international.objects.filter(abs_titles='focal_pic_news')
        focal_pictures_news = international.objects.filter(abs_titles='focal_pictures_news')
        # 军事
        military_news = international.objects.filter(abs_titles='military_news')
        military_pic_news = international.objects.filter(abs_titles='military_pic_news')
        # 热门
        hot_news = international.objects.filter(abs_titles='hot_news')
        # 最新
        latest_news = international.objects.filter(abs_titles='latest_news')

        contex = {
            # 热点
            'img_news':img_news,
            'instant_news':instant_news,
            # 焦点
            'focal_news1':focal_news[:6],
            'focal_news2':focal_news[6:],
            'focal_pic_news':focal_pic_news,
            'focal_pictures_news':focal_pictures_news,
            # 军事
            'military_news1':military_news[:6],
            'military_news2':military_news[6:],
            'military_pic_news':military_pic_news,
            # 热门
            'hot_news':hot_news,
            # 最新新闻
            'latest_news1':latest_news[:10],
            'latest_news2':latest_news[10:],
            'username': request.session.get("username"),
        }
        return render(request,"international.html",contex)        

