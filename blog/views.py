<<<<<<< HEAD
from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 857150f6928d235e42023773913c9a9a034aa261
