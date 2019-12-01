'''
@Author: 华豪
@Date: 2019-12-01 14:31:33
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-01 14:46:22
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from internet.models import internet

# Create your views here.
def internet_news(request):
    if request.method == "GET":
        contex = {}
        return render(request,"internet.html",contex) 
