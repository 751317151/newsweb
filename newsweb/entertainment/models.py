'''
@Author: 华豪
@Date: 2019-11-29 16:38:10
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-29 16:40:12
'''
from django.db import models

# Create your models here.
class entertainment(models.Model):
    titles = models.CharField(default=0,max_length=255)
    urls = models.CharField(default=0,max_length=255)
    abs_titles = models.CharField(default=0,max_length=255)
    imgurls = models.CharField(default=0,max_length=255)