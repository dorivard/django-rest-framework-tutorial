# -*- coding: utf-8 -*-
"""
This module contains the 

"""
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)