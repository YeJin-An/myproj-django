from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from news.models import News
from blog.serializers import PostSerializer ,NewsAdminSerializer

import json
from django.http import HttpRequest, HttpResponse

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    # serializer_class = PostSerializer
    def get_serializer_class(self):
        return NewsAdminSerializer
        # 함수의 이름을 넣어주는 역활??

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.query_params.get("query","")
        if query:
            qs = qs.filter(title_ic=query)
        year = self.request.query_params.get("year","")
        if year:
            qs = qs.filter(title_ic=year)
        return qs

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

# article_list = ListAPIView.as_view(
#     queryset = News.objects.all(),
#     serializer_class = PostSerializer
# )

# def Article_list(request):
#     qs = News.objects.alll()
#     serializer = PostSerializer(qs,many=True)
#     data = serializer.data
#     # data = [
#     #     {"id":article.id, 
#     #     "title":article.title, 
#     #     "content":article.content,
#     #     "photo": request.build_absolute_url(article.photo.url) if article.photo else None,
#     #     }
#     #     for article in qs
#     # ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)