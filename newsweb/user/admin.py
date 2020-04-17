'''
@Author: 华豪
@Date: 2019-12-10 21:38:56
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2020-04-17 20:02:48
'''
from django.contrib import admin
from user.models import user

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'password',
        'reg_time',
        'last_login_time',
    ]
    search_fields = ('email','username',)
    list_per_page = 5
    list_editable = ('email','username','password',)

admin.site.register(user,userAdmin)
admin.AdminSite.site_header ='新闻推荐系统后台管理'
admin.AdminSite.site_title = '新闻推荐系统后台管理'
