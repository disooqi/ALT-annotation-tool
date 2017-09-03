#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
created on 2017 Sep 03
by disooqi
'''

from django.shortcuts import render
from django.http import HttpResponse

from django_project import settings

# Create your views here.
def index(request):
    proj = settings.client.projects.get('2892')
    aa_spider = proj.spiders.get('almasryalyoum')
    job_key =  aa_spider.jobs.list()[0]['key']
    last_job = aa_spider.jobs.get(job_key)
    print last_job.items.list()[0]


    # most_common_tokens = Token.objects.order_by('-freq')[(p * 10) - 10:p * 10]

    context = {'last_news_articles': last_job.items.list(), 'article_source':u'المصري اليوم'}
    return render(request, 'gornany/index.html', context)
