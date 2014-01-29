# -*- coding: utf-8 -*-
"""
This module contains the serializers for the REST API.

"""
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'first_name', 'last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')