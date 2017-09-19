# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article
from src.app import BuzzfeedApp
from django.shortcuts import render

def index(request):

    return render(request, 'index.html', {})
