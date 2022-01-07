from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import review_list,review_new, ReviewViewSet


app_name = "shop"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("review/new", review_new, name = "review_new"),
    path("review/", review_list, name='review_list'),
    path("api/", include(router.urls)),
]