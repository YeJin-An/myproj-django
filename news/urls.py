from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet

router = DefaultRouter()
router.register("news", NewsViewSet)

urlpatterns = [
  path("articles.json", news.article_list),
  path("api/", include(router.urls)),
]

# TOCO 아래 token view는 accounts앱 ㅐ에 두는 것이 맞습니다.

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]