# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-22 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuzzfeedSimulatorApp', '0003_auto_20170922_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.CharField(default='https://pbs.twimg.com/profile_images/600060188872155136/st4Sp6Aw.jpg', max_length=1000),
        ),
    ]
