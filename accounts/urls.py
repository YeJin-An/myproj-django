from django.urls import path
from accounts.views import TokenObtainPairView, TokenRefreshView, SignupAPIView

app_name = "accounts"

urlpatterns = []

urlpatterns += [
    path('api.signup', SignupAPIView.as_View(), name="SignupAPIView")
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]