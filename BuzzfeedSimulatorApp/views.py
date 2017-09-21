# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article
from .utils import BuzzfeedSimulator, ImageScraper
from django.shortcuts import render

app = BuzzfeedSimulator()
scraper = ImageScraper()

def index(request):
    title = app.run()
    image = scraper.get_image(title)

    article = Article(title=title, image_url=image, content="Descriptions comin soon")
    article.save()
    # print type(image

    articles = Article.objects.order_by('created_date').reverse()
    return render(request, 'index.html', {'articles': articles})
