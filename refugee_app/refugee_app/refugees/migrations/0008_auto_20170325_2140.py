# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-25 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refugees', '0007_comment_body_stemmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='WordCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refugees.CategoryType')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='word_category',
            field=models.ManyToManyField(to='refugees.WordCategory'),
        ),
    ]
