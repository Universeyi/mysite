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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import datetime
# Create your views here.


def detail(request, my_args):
    post = Article.objects.all()
    str = ("title = %s,\n category = %s,\n date_time = %s,\n content = %s\n"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
    
#TODO 这里只是为了测试方便，将queryset转换为list进行操作，以后希望将更新的信息保存在数据库中。
def home(request):
    contact_list = Article.objects.all()
    paginator = Paginator(contact_list, 7)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'post_list': contacts})


    # post_list= Article.objects.all()
    # return render(request, 'home.html', {'post_list' : post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})
def pa(request):
    getBestAnswer()
    return HttpResponse('已经获取网页设计下的20个回答')
def li(request):
    # def getContentDigest(mo):
    #     content = mo.content
    #     if len(content) > 107:
    #         content = content[0:108]
    #     return content
    i = 0
    for mo in Article.objects.all():
        mo.url =  html2text(mo.content)
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