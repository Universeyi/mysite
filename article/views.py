# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
#import datetime
# Create your views here.


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s,\n category = %s,\n date_time = %s,\n content = %s\n"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})



def current_datetime(request):
    now = datetime.now()
    t = get_template('time.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
