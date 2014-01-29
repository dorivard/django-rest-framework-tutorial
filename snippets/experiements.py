# -*- coding: utf-8 -*-
"""
This module contains the 

"""
from __future__ import unicode_literals, absolute_import


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.compat import BytesIO


# create some instances
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

# lets serialize them into naitve python data type
serializer = SnippetSerializer(snippet)
print serializer.data
# lets serialize them into JSON
content = JSONRenderer().render(serializer.data)
print content

# deserialize the JSON into python data type
stream = BytesIO(content)
data = JSONParser().parse(stream)

# native data type to full object instance
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.object

# serialize a queryset
serializer = SnippetSerializer(Snippet.objects.all(), many=True)

"""
curl http://127.0.0.1:8000/api/snippets/?format=json

curl http://127.0.0.1:8000/api/snippets/

curl http://127.0.0.1:8000/api/snippets/1/

curl http://127.0.0.1:8000/api/users/

curl -X POST http://127.0.0.1:8000/api/snippets/ -d "code=print 789" -u test:test1234
"""