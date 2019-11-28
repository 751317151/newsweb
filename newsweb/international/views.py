'''
@Author: 华豪
@Date: 2019-11-28 17:47:03
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-28 17:55:33
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from international.models import international

# Create your views here.
def international_news(request):
    if request.method == "GET":
        contex = {}
        return render(request,"international.html",contex)        

