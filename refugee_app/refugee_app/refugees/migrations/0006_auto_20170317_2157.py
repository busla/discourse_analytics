# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-17 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refugees', '0005_auto_20170309_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('fb_id', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='fb_comment_id',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='fb_created_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='fb_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='refugees.FBAuthor'),
        ),
    ]
