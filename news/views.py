from rest_framework import viewsets
from news.models import News
from blog.serializers import PostSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = PostSerializer