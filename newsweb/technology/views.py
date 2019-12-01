'''
@Author: 华豪
@Date: 2019-12-01 14:31:22
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-01 14:46:01
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from technology.models import technology

# Create your views here.
def technology_news(request):
    if request.method == "GET":
        contex = {}
        return render(request,"technology.html",contex) 
