#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.


lastSaveTime = datetime(2016,6,9,12,00).day

class Article(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)  #博客题目
    url = models.CharField(max_length = 200) #url
    author = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

    def save(self, *args, **kwargs):
        lastSaveTime = datetime.now().day
        super(Article, self).save()
