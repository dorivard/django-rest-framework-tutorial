# -*- coding: utf-8 -*-
"""
This module contains the 

"""
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)