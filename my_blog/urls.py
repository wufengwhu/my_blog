# coding=utf-8
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from userena.forms import SignupForm

from article.views import HomePageView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView
from article.views import RSSFeed, DefaultArticleView
from biportal.views import FormHorizontalView

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'my_blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls)),

                       (r'^messages/', include('userena.contrib.umessages.urls')),
                       (r'^i18n/', include('django.conf.urls.i18n')),
                       # url(r'^$', 'article.views.home',name = 'home'),  #由于目前只有一个app, 方便起见, 就不设置include了
                       # url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'), #这个正则表达式的意思是将传入的一位或者多位数字作为参数传递到views中的detail作为参数, 其中?P<my_args>定义名称用于标识匹配的内容
                       # url(r'^$', 'article.views.home'),
                       url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
                       url(r'^archives/$', 'article.views.archives', name='archives'),
                       url(r'^aboutme/$', 'article.views.about_me', name='aboutme'),
                       url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name='search_tag'),
                       url(r'^search/$', 'article.views.blog_search', name='search'),
                       url(r'^feed/$', RSSFeed(), name="RSS"),  # 新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
                       url(r'^test_bootstarp3', DefaultArticleView.as_view(), name="test"),

                       url(r'^$', HomePageView.as_view(), name='home'),
                       url(r'^promo$', 'profiles.views.promo', name='promo'),
                       url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
                       url(r'^form$', DefaultFormView.as_view(), name='form_default'),
                       url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
                       url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
                       url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
                       url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
                       url(r'^pagination$', PaginationView.as_view(), name='pagination'),
                       url(r'^misc$', MiscView.as_view(), name='misc'),
                       url(r'^big_trans/$', 'biportal.views.big_trans', name='big_trans'),
                       url(r'^add/$', FormHorizontalView.as_view(), name='form_horizontal'),

                       # # Demo Override the signup form with our own, which includes a first and last name.
                       (r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupForm,
                                                                        # 'template_name': 'signup.html',
                                                                        'success_url': '/big_trans/'},

                        ),

                       (r'^accounts/', include('userena.urls')),
                       )
