# -*- coding: utf-8 -*-
"""
This module contains the 

"""
from __future__ import unicode_literals, absolute_import

from django.forms import widgets

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# Serialize the model into native python data type. Here it is going to be a
# dictionary.
class SnippetSerializer(serializers.ModelSerializer):
    # pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    # title = serializers.CharField(required=False,
    #                               max_length=100)
    # code = serializers.CharField(widget=widgets.Textarea,
    #                              max_length=100000)
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
    #                                    default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES,
    #                                 default='friendly')
    #
    # def restore_object(self, attrs, instance=None):
    #     """
    #     Create or update a new snippet instance, given a dictionary
    #     of deserialized field values.
    #
    #     Note that if we don't define this method, then deserializing
    #     data will simply return a dictionary of items.
    #     """
    #     if instance:
    #         # Update existing instance
    #         instance.title = attrs.get('title', instance.title)
    #         instance.code = attrs.get('code', instance.code)
    #         instance.linenos = attrs.get('linenos', instance.linenos)
    #         instance.language = attrs.get('language', instance.language)
    #         instance.style = attrs.get('style', instance.style)
    #         return instance
    #
    #     # Create new instance
    #     return Snippet(**attrs)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')