# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bcv', '0002_auto_20170605_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['publication_date']},
        ),
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail'),
        ),
    ]
