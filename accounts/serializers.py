from unicodedata import name
from rest_framework_simplejwt.serializers import (
  TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
  TokenRefreshSerializer as OrigTokenRefreshSerializer
)
from typing import Dict

class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user)-> Dict:
    token = super().get_token(user)
    token['username'] = user.username
    token['firstname'] = user.first_name
    token['list_name'] = user.list_name
    return token



class TokenRefreshSerializer(OrigTokenRefreshSerializer):
  pass




