# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000, default='')
    content = models.TextField(max_length=2500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
