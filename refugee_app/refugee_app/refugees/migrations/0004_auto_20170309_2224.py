# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-09 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugees', '0003_comment_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
