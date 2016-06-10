# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from article.tp import getBestAnswer
from html2text import html2text
#import datetime
# Create your views here.


def detail(request, my_args):
    post = Article.objects.all()
    str = ("title = %s,\n category = %s,\n date_time = %s,\n content = %s\n"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
    
#TODO 这里只是为了测试方便，将queryset转换为list进行操作，以后希望将更新的信息保存在数据库中。
def home(request):
    #post_list = list(Article.objects.all()).append(getBestAnserwer())#    #获取全部的Article对象
    post_list= Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})
    #return HttpResponse(post_list[0].content)

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})
def pa(request):
    getBestAnswer()

def li(request):
    # def getContentDigest(mo):
    #     content = mo.content
    #     if len(content) > 107:
    #         content = content[0:108]
    #     return content
    i = 0
    for mo in Article.objects.all():
        mo.content =  html2text(mo.content)
        i = 1+i
    return HttpResponse("成功完成%d个元素的操作"%i)
# def test(request) :
#     return render(request, 'test.html', {'current_time': datetime.now()})
#


def current_datetime(request):
    now = datetime.now()
    t = get_template('time.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
#
# post_list = list(Article.objects.all()).append(getBestAnserwer())
# print(post_list[0].content)