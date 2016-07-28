# coding=utf-8

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
STATUS_CHOICES = (('d', 'Draft'),
                  ('p', 'Published'),
                  ('w', 'Withdrawn'),
                  )


class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name


class ArticleAdmin(admin.ModelAdmin):

    def make_published(modeladmin, request, queryset):
        queryset.update(status='p')

    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]
    make_published.short_description = "Mark selected stories as published"


class Article(models.Model):
    """docstring for ClassName"""
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客分类
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

admin.site.register(Article, ArticleAdmin)
