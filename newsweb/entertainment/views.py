'''
@Author: 华豪
@Date: 2019-11-29 16:38:10
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-29 23:10:05
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from entertainment.models import entertainment

# Create your views here.
def entertainment_news(request):
    if request.method == "GET":
        # 热点
        img_news = entertainment.objects.filter(abs_titles='tupian')
        instant_news = entertainment.objects.filter(abs_titles='instant_news')
        # 焦点
        focal_news = entertainment.objects.filter(abs_titles='focal_news')
        focal_pic_news = entertainment.objects.filter(abs_titles='focal_pic_news')
        # 明星
        star_news = entertainment.objects.filter(abs_titles='star_news')
        star_pic_news = entertainment.objects.filter(abs_titles='star_pic_news')
        rumours_news = entertainment.objects.filter(abs_titles='rumours_news')
        variety_video_news = entertainment.objects.filter(abs_titles='variety_video_news')
        # 电影
        movie_news = entertainment.objects.filter(abs_titles='movie_news')
        movie_pic_news = entertainment.objects.filter(abs_titles='movie_pic_news')
        movie_features_news = entertainment.objects.filter(abs_titles='movie_features_news')
        # 电视
        TV_news = entertainment.objects.filter(abs_titles='TV_news')
        TV_pic_news = entertainment.objects.filter(abs_titles='TV_pic_news')
        hot_tv_news = entertainment.objects.filter(abs_titles='hot_tv_news')
        hot_tv_comments_news = entertainment.objects.filter(abs_titles='hot_tv_comments_news')

        contex = {
            # 热点
            'img_news':img_news,
            'instant_news':instant_news,
            # 焦点
            'focal_news1':focal_news[:6],
            'focal_news2':focal_news[6:],
            'focal_pic_news':focal_pic_news,
            # 明星
            'star_news1':star_news[:6],
            'star_news2':star_news[6:12],
            'star_news3':star_news[12:],
            'star_pic_news':star_pic_news,
            'rumours_news':rumours_news,
            'variety_video_news':variety_video_news,
            # 电影
            'movie_news1':movie_news[:6],
            'movie_news2':movie_news[6:],
            'movie_pic_news':movie_pic_news,
            'movie_features_news':movie_features_news,
            # 电视
            'TV_news1':TV_news[:6],
            'TV_news2':TV_news[6:],
            'TV_pic_news':TV_pic_news,
            'count':[hot_tv_news[:5],hot_tv_news[5:10],hot_tv_news[10:15],hot_tv_news[15:]],
            'hot_tv_comments_news':hot_tv_comments_news,
        }
        return render(request,"entertainment.html",contex) 