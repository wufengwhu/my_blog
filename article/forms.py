# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bootstrap3.tests import TestForm
from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from .models import Article

RADIO_CHOICES = (
    ('1', 'Radio 1'),
    ('2', 'Radio 2'),
)

MEDIA_CHOICES = (
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )
     ),
    ('unknown', 'Unknown'),
)

DB_CHOICES = (
    ('NoSQL', (
        ('hiveDB', 'HiveDB'),
        ('mongoDB', 'MongoDB'),
    )),

    ('MySQL', (
        ('38', 'mysql-3rd_platform-master    [etlqry @ mysql-3rd.int.yihaodian.com:3306/3rd_platform]'),
    )),

    ('Oracle', (
        ('6', 'oracle-ETL    [ETL @ ex4-dw1.int.yihaodian.com:1521/edwstd01]'),
    )),
)
EXTRACT_METHODS = (
    ('1', 'SQOOP_MR'),
    ('2', 'SQOOP_JDBC'),
    ('3', 'YHD'),
)


class ContactForm(TestForm):
    subject = forms.CharField(
        max_length=100,
        help_text='my_help_text',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'placeholdertest'}),
    )
    job_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 85,
                                                                   'placeholder': '请简要描述作业目的'}),
                                      max_length=160, required=False,
                                      label='作业简述')
    db_s_infos = forms.CharField(widget=forms.Select(choices=DB_CHOICES, attrs={'id': 'SRC_DBID'}),
                                 required=True, label='源库')

    db_d_infos = forms.CharField(widget=forms.Select(choices=DB_CHOICES, attrs={'id': 'DST_DBID'}),
                                 required=True, label='目标库')

    extract_options = forms.CharField(widget=forms.Select(choices=EXTRACT_METHODS,
                                                          attrs={'id': 'EXTRACT_OPTIONS'}),
                                      required=True, label='抽取方式')
    extract_duration = forms.DurationField(initial=10, required=False, label='预计使用时长',
                                           help_text='<i class=\"fa fa-info\"> 单位分钟</i>')


class ContactBaseFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(ContactBaseFormSet, self).add_fields(form, index)

    def clean(self):
        super(ContactBaseFormSet, self).clean()
        raise forms.ValidationError("This error was added to show the non form errors styling")


ContactFormSet = formset_factory(TestForm, formset=ContactBaseFormSet,
                                 extra=2,
                                 max_num=4,
                                 validate_max=True)


class FilesForm(forms.Form):
    text1 = forms.CharField()
    file1 = forms.FileField()
    file2 = forms.FileField(required=False)
    file3 = forms.FileField(widget=forms.ClearableFileInput)
    file5 = forms.ImageField()
    file4 = forms.FileField(required=False, widget=forms.ClearableFileInput)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()
    sender = forms.EmailField(label='Sender © unicode',
                              help_text='E.g., "w_feng_1986@126.com"')
    b_one = forms.IntegerField(
        error_messages={
            'required': 'Please enter a valid number.'
        },
        label='NumberOne',
        required=True,
        help_text='e.g. 266492'
    )

    b_two = forms.IntegerField(
        error_messages={
            'required': 'Please enter a valid number.'
        },
        label='NumberTwo',
        required=True,
        help_text='e.g. 262865',
    )

    def clean_b_one(self):
        self.validate_form(self.cleaned_data['b_one'])

    def clean_b_two(self):
        self.validate_form(self.cleaned_data['b_two'])

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
