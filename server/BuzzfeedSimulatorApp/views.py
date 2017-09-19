# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article
# from src.app import BuzzfeedSimulator
from django.shortcuts import render

# app = BuzzfeedSimulator()

def index(request):

    article = Article(title="First Blog", content="This is the body")
    article.save()

    articles = Article.objects.order_by('created_date').reverse()
    return render(request, 'index.html', {'articles': articles})
