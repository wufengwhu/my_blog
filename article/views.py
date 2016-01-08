# coding=utf-8
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.syndication.views import Feed  # 注意加入import语句
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from userena.forms import SignupForm

from article.models import Article
from .forms import ContactForm, FilesForm, ContactFormSet, ArticleForm


# Create your views here.

class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content


def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    paginator = Paginator(post_list, 5)  # 每页显示两个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404

    # str = ("title = %s, category = %s, date_time = %s, content = %s" 
    #     % (post.title, post.category, post.date_time, post.content))
    return render(request, 'post.html', {'post': post})


def about_me(request):
    return render(request, 'aboutme.html')


def big_trans(request):
    return render(request, 'big_trans.html')


def big_trans_test(request):
    return render(request, 'big_trans_test.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home_backup.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'big_trans.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context


class DefaultFormsetView(FormView):
    template_name = 'formset.html'
    form_class = ContactFormSet


class DefaultArticleView(FormView):
    template_name = 'bootstrap3_test.html'
    form_class = ArticleForm


class DefaultFormView(FormView):
    template_name = 'form.html'
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = 'form_by_field.html'
    form_class = ContactForm



class FormInlineView(FormView):
    template_name = 'form_inline.html'
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = 'form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        return context

    def get_initial(self):
        return {
            'file4': fieldfile,
        }


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = "/big_trans/"

    def form_valid(self, form_class):
        user = form_class.save()



class PaginationView(TemplateView):
    template_name = 'pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(10000):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'misc.html'
