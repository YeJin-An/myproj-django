from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet

router = DefaultRouter()
router.register("news", NewsViewSet)

urlpatterns = [
  path("api/", include(router.urls)),
]
