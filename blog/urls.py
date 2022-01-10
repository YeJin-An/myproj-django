<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet

app_name = 'blog'

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
=======
from django.urls.resolvers import URLPattern



from django.urls import path, include

urlpatterns = [

>>>>>>> 857150f6928d235e42023773913c9a9a034aa261
]