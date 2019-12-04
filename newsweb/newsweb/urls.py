'''
@Author: 华豪
@Date: 2019-10-25 09:29:27
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-03 16:49:42
'''
"""newsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from index import views as index_views
from sports import views as sports_views
from china import views as china_views
from international import views as international_views
from entertainment import views as entertainment_views
from military import views as military_views
from technology import views as technology_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_views.index_news),
    path('china',china_views.china_news),
    path('international',international_views.international_news),
    path('entertainment',entertainment_views.entertainment_news),
    path('sports', sports_views.sports_news),
    path('military',military_views.military_news),
    path('technology',technology_views.technology_news),
]
