# -*- coding:utf-8 -*-
# from __future__ import unicode_literals, print_function
from zhihu_oauth import ZhihuClient
# from zhihu_oauth.oauth import zhihu_oauth
# from zhihu_oauth.exception import NeedCaptchaException
from article.models import Article
from datetime import datetime
import os
from article.models import lastSaveTime
from html2text import html2text

def getBestAnswer():
    if lastSaveTime != datetime.now().day:
        getLatestBestAnserwerAndSave()

class ansItem():
    def __init__(self,answer):
        self.qTitle = answer.question.title
        self.content = html2text(answer.content)
        self.authorWithHeadLine= str(answer.author.name) + "  " + str(answer.author.headline)

    def getContentDigest(self):
        content = self.content
        if len(content) > 107:
            content = content[0:108]
        return content


def getLatestBestAnserwerAndSave():
    # phoneNum = '+8613096348217'
    # pw = '2015141463222'

    ans_num = 10
    i=0


    TOKEN_FILE = 'token.pkl'
    client = ZhihuClient()

    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        client.login_in_terminal()
        client.save_token(TOKEN_FILE)

    # try:
    #     client.login(phoneNum, pw)
    # except NeedCaptchaException:
    #     # 保存验证码并提示输入，重新登录
    #     with open('a.gif', 'wb') as f:
    #         f.write(client.get_captcha())
    #     captcha = input('please input captcha:')
    #     client.login(phoneNum, pw, captcha)

    java = client.topic(19561132)
    BA = java.best_answers
    for answ in BA:
        ansItem2artical(ansItem(answ)).save()
        i = i+1

        if i==ans_num:
            break
    # baList = list(map(ansItem2artical,baList))
    # return baList

def ansItem2artical(ansItem):
    article = Article()
    article.title = ansItem.qTitle
    article.author = ansItem.authorWithHeadLine
    article.category = 'Java'
    article.content = ansItem.getContentDigest()
    return article

# for ansItem in getBestAnserwer():
#     print(ansItem.qTitle)
#     print(ansItem.authorWithHeadLine)
#     print(ansItem.getContentDigest())
#     print("-----------------------------")
