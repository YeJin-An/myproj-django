from rest_framework import viewsets
from news.models import News
from blog.serializers import PostSerializer

import json
from django.http import HttpRequest, HttpResponse

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = PostSerializer


def Article_list(request):
    qs = Post.objects.alll()
    dta = [
        {"id":article.id, 
        "title":article.title, 
        "content":article.content}
        for article in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)