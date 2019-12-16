'''
@Author: 华豪
@Date: 2019-11-29 16:38:10
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-13 21:45:25
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
        # 音乐
        music_news = entertainment.objects.filter(abs_titles='music_news')
        music_pic_news = entertainment.objects.filter(abs_titles='music_pic_news')
        top_music_news1 = entertainment.objects.filter(abs_titles='top_music_news1')
        top_music_news2 = entertainment.objects.filter(abs_titles='top_music_news2')
        china_music_news1 = entertainment.objects.filter(abs_titles='china_music_news1')
        china_music_news2 = entertainment.objects.filter(abs_titles='china_music_news2')
        # 电影
        variety_news = entertainment.objects.filter(abs_titles='variety_news')
        variety_pic_news = entertainment.objects.filter(abs_titles='variety_pic_news')
        variety_click_news = entertainment.objects.filter(abs_titles='variety_click_news')
        # 图片
        picture_news = entertainment.objects.filter(abs_titles='picture_news')
        # 最新新闻
        latest_news = entertainment.objects.filter(abs_titles='latest_news')

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
            # 音乐
            'music_news1':music_news[:6],
            'music_news2':music_news[6:],
            'music_pic_news':music_pic_news,
            'top_music_news1':top_music_news1,
            'top_music_news2':top_music_news2,
            'top_music_news':zip(top_music_news1,top_music_news2),
            'china_music_news1':china_music_news1,
            'china_music_news2':china_music_news2,
            'china_music_news':zip(china_music_news1,china_music_news2),
            # 综艺
            'variety_news1':variety_news[:6],
            'variety_news2':variety_news[6:],
            'variety_pic_news':variety_pic_news,
            'variety_click_news':variety_click_news,
            # 图片
            'picture_news':picture_news,
            # 最新新闻
            'latest_news1':latest_news[:10],
            'latest_news2':latest_news[10:],
            'username': request.session.get("username"),
        }
        return render(request,"entertainment.html",contex) 