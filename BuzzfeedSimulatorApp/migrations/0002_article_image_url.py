# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuzzfeedSimulatorApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
