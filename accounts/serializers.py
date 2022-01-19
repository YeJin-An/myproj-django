from unicodedata import name
from accounts.views import User
from rest_framework.serializers import serializer
from rest_framework_simplejwt.serializers import (
  TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
  TokenRefreshSerializer as OrigTokenRefreshSerializer
)

class UserCreationSerializer(serializer.ModelSerializer):
  password = serializers.CharField(write_only=True , required=True)
  password = serializers.CharField(write_only=True , required=True)

  class Meta:
    model = User
    fields = ["username"]

  def validate(self, attrs):
    data = super().validate(attrs)
    data["username"] = self.user.username
    data["first_name"] = self.user.first_name
    data["last_name"] = self.user.last_name
    return data

  # @classmethod
  # def get_token(cls, user)-> Dict:
  #   token = super().get_token(user)
  #   token['username'] = user.username
  #   token['firstname'] = user.first_name
  #   token['list_name'] = user.list_name
  #   return token



class TokenRefreshSerializer(OrigTokenRefreshSerializer):
  pass




