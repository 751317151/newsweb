'''
@Author: 华豪
@Date: 2019-12-01 14:31:33
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-12-01 14:33:18
'''
from django.db import models

# Create your models here.
class internet(models.Model):
    titles = models.CharField(default=0,max_length=255)
    urls = models.CharField(default=0,max_length=255)
    abs_titles = models.CharField(default=0,max_length=255)
    imgurls = models.CharField(default=0,max_length=255)