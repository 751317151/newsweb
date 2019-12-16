'''
@Author: 华豪
@Date: 2019-12-10 21:38:56
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-12 20:07:49
'''
from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField()
    username = models.CharField(default=0,max_length=20)
    password = models.CharField(default=0,max_length=20)
    reg_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(auto_now=True)

    china_count = models.IntegerField(default=0)
    international_count = models.IntegerField(default=0)
    entertainment_count = models.IntegerField(default=0)
    sport_count = models.IntegerField(default=0)
    technology_count = models.IntegerField(default=0)
    military_count = models.IntegerField(default=0)
   