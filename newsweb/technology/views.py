'''
@Author: 华豪
@Date: 2019-12-01 14:31:22
@E-Mail: hh@huahaohh.cn
@LastEditors  : 华豪
@LastEditTime : 2020-03-01 14:45:40
'''
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from technology.models import technology

# Create your views here.
def technology_news(request):
    if request.method == "GET":
        username = request.session.get("username")
        if username:
            # 热点
            img_news = technology.objects.filter(abs_titles='tupian')
            # 最新新闻
            latest_news = technology.objects.filter(abs_titles='latest_news')
            internet_news = technology.objects.filter(abs_titles='internet_news')
            middle_news = technology.objects.filter(abs_titles='middle_news')
            # 科学探索
            science_news = technology.objects.filter(abs_titles='science_news')
            technology_video_news = technology.objects.filter(abs_titles='technology_video_news')
            technology_news = technology.objects.filter(abs_titles='technology_news')
            # 通信
            communication_news = technology.objects.filter(abs_titles='communication_news')
            middle_focus_news = technology.objects.filter(abs_titles='middle_focus_news')
            company_news = technology.objects.filter(abs_titles='company_news')
            # 手机
            iphone_news = technology.objects.filter(abs_titles='iphone_news')
            android_news = technology.objects.filter(abs_titles='android_news')
            shouji_middle_news = technology.objects.filter(abs_titles='shouji_middle_news')
            shouji_right_news = technology.objects.filter(abs_titles='shouji_right_news')
            # 数码
            panel_computer_news = technology.objects.filter(abs_titles='panel_computer_news')
            E_book_news = technology.objects.filter(abs_titles='E_book_news')
            shuma_middle_news = technology.objects.filter(abs_titles='shuma_middle_news')
            new_computer_news = technology.objects.filter(abs_titles='new_computer_news')
            # 科学
            universe_news = technology.objects.filter(abs_titles='universe_news')
            history_news = technology.objects.filter(abs_titles='history_news')
            science_middle_news = technology.objects.filter(abs_titles='science_middle_news')
            science_discovery_video_news = technology.objects.filter(abs_titles='science_discovery_video_news')
            science_discovery_news = technology.objects.filter(abs_titles='science_discovery_news')
            hot_click_news = technology.objects.filter(abs_titles='hot_click_news')

            contex = {
                # 热点
                'img_news':img_news,
                # 最新新闻
                'latest_news1':latest_news[:10],
                'latest_news2':latest_news[10:],
                'internet_news':internet_news,
                'middle_news':[middle_news[:6],middle_news[6:11],middle_news[11:16],middle_news[16:]],
                # 科学探索
                'science_news':science_news,
                'technology_video_news':technology_video_news,
                'technology_news':technology_news,
                # 通信
                'communication_news':communication_news,
                'middle_focus_news':[middle_focus_news[:6],middle_focus_news[6:11],middle_focus_news[11:]],
                'company_news':company_news,
                # 手机
                'iphone_news':iphone_news,
                'android_news':android_news,
                'shouji_middle_news':[shouji_middle_news[:6],shouji_middle_news[6:11],shouji_middle_news[11:]],
                'shouji_right_news':shouji_right_news,
                # 数码
                'panel_computer_news':panel_computer_news,
                'E_book_news':E_book_news,
                'shuma_middle_news':[shuma_middle_news[:6],shuma_middle_news[6:11],shuma_middle_news[11:]],
                'new_computer_news':new_computer_news,
                # 科学
                'universe_news':universe_news,
                'history_news':history_news,
                'science_middle_news':[science_middle_news[:6],science_middle_news[6:11],science_middle_news[11:]],
                'science_discovery_video_news':science_discovery_video_news,
                'science_discovery_news':science_discovery_news,
                'hot_click_news':hot_click_news,
                'username': request.session.get("username"),
            }
            return render(request,"technology.html",contex) 
        else:
            return HttpResponseRedirect("/login")
