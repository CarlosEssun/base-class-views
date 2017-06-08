# -*- coding: utf8 -*-
from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.

# costom  view list


class auhtorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')  # 设置查找


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)  # 过滤器
    date_hierarchy = 'publication_date'  # 记录上方显示年份
    ordering = ('-publication_date',)   # 降序排列
    # fields = ('title', 'authors', 'publisher')  # 设置可编辑字段
    fields_horizontal = ('authors',)
    raw_id_fields = ('publisher',)  # 非下拉列表，而是以查找字段的方式


# 将models 注册到管理页面
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, auhtorAdmin)
