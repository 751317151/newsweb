'''
@Author: 华豪
@Date: 2019-11-27 15:48:22
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-27 15:49:29
'''
from django.db import models

# Create your models here.
class china(models.Model):
    titles = models.CharField(default=0,max_length=255)
    urls = models.CharField(default=0,max_length=255)
    abs_titles = models.CharField(default=0,max_length=255)
    imgurls = models.CharField(default=0,max_length=255)