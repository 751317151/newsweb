'''
@Author: 华豪
@Date: 2019-12-01 14:30:10
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-01 14:33:09
'''
from django.db import models

# Create your models here.
class military(models.Model):
    titles = models.CharField(default=0,max_length=255)
    urls = models.CharField(default=0,max_length=255)
    abs_titles = models.CharField(default=0,max_length=255)
    imgurls = models.CharField(default=0,max_length=255)