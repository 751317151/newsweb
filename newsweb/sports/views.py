'''
@Author: 华豪
@Date: 2019-10-28 10:43:56
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-03 17:57:08
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from sports.models import sports

# Create your views here.

def sports_news(request):
    if request.method == "GET":

        news = sports.objects.filter(abs_titles='top_sports_news')
        img_news = sports.objects.filter(abs_titles='tupian')
        world_football_news = sports.objects.filter(abs_titles='world_football')
        star_news = sports.objects.filter(abs_titles='star_news')
        china_football_news = sports.objects.filter(abs_titles='china_football')
        player_news = sports.objects.filter(abs_titles='player_news')
        NBA_news = sports.objects.filter(abs_titles='NBA_news')
        video_news = sports.objects.filter(abs_titles='video_news')
        CBA_news = sports.objects.filter(abs_titles='CBA_news')
        focus_events = sports.objects.filter(abs_titles='focus_events')
        other_sports_news = sports.objects.filter(abs_titles='other_sports')
        hot_articles = sports.objects.filter(abs_titles='hot_articles')
        latest_news = sports.objects.filter(abs_titles='latest_news')
        contex = {
            "news1":news[:7],
            "news2":news[7:14],
            "news3":news[14:],
            'img_news':img_news,
            'world_football_news1':world_football_news[:6],
            'world_football_news2':world_football_news[6:12],
            'star_news':star_news,
            'china_football_news1':china_football_news[:6],
            'china_football_news2':china_football_news[6:12],
            'player_news':player_news,
            'NBA_news1':NBA_news[:6],
            'NBA_news2':NBA_news[6:12],
            'CBA_news1':CBA_news[:6],
            'CBA_news2':CBA_news[6:12],
            'video_news':video_news,
            'focus_events':focus_events,
            'other_sports_news1':other_sports_news[:6],
            'other_sports_news2':other_sports_news[6:12],
            'hot_articles':hot_articles,
            'latest_news1':latest_news[:10],
            'latest_news2':latest_news[10:]
            }
        return render(request,"sports.html",contex)