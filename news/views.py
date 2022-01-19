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
    
    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때, 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지정을 지원합니다.
        serializer.save(author=self.request.user, ip=)