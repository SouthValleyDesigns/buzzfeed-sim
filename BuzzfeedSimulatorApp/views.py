# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article
from .utils import BuzzfeedSimulator
from django.shortcuts import render

app = BuzzfeedSimulator()

def index(request):
    title = app.run()

    article = Article(title=title, content="Descriptions comin soon")
    article.save()

    articles = Article.objects.order_by('created_date').reverse()
    return render(request, 'index.html', {'articles': articles})
