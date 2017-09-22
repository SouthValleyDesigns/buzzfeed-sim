# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article
from .utils import BuzzfeedSimulator, ImageScraper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

app = BuzzfeedSimulator()
scraper = ImageScraper()

# def index(request):
#     articles = Article.objects.order_by('created_date').reverse()
#     return render(request, 'index.html', {'articles': articles})


def index(request):
    articles = Article.objects.order_by('created_date').reverse()

    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'articles':articles})


def create(request):
    title = app.run()
    image = scraper.get_image(title)
    print title
    print image

    article = Article(title=title.encode('utf-8'), image_url=image, content="Descriptions comin soon")
    article.save()
    return render(request, 'redirect.html', {})
