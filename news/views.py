from nntplib import ArticleInfo
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from news.models import News
from blog.serializers import PostSerializer ,NewsAdminSerializer

import json
from django.http import HttpRequest, HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    # serializer_class = PostSerializer
    def get_serializer_class(self):
        return NewsAdminSerializer
        # 함수의 이름을 넣어주는 역활??
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_permission(self):
        #if self.request.method in ("POST","PUT","PATCH","DELETE"):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
        