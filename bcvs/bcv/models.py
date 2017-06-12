# -*- coding: utf8 -*-
from __future__ import unicode_literals

from django.db import connection, models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(
        blank=True, null=True, verbose_name='e-mail')  # blank表示可以不填。
    last_accessed = models.DateTimeField()

    # verbose 为字段打上tag

    def __unicode__(self):
        return self.first_name


# 自定义管理器
class PythonBookManager(models.Manager):
    def get_queryset(self):
        # 调用父类的方法，在原来返回的QuerySet的基础上返回新的QuerySet
        return super(PythonBookManager, self).get_queryset().filter(title__icontains ='openstack')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    objects = models.Manager()
    book_objects = PythonBookManager()

    # def date_valide(self):
    #     import datetime
    #     if self.publication_date >= datetime.date(2015, 01, 01):
    #         return "good"
    #     else:
    #         return "bad"

    # def get_title_or_author(self):
    #     return u'%s %s' % (self.title, self.authors)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['publication_date']  # 定义源数据: 排序规则