from unicodedata import name
from accounts.views import User
from rest_framework.serializers import serializer
from django.contrib.auth import get_user_model 
from django.contrib.auth.password 
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
    if attrs["password"] != attrs["password2"]:
      raise serializers.ValidationError("동일한 암호를 지정해주세요.")
    return attrs

  def create(self, validated_data):
    validated_data["username"]
    validated_data["password"]

    new_user = User(username = username)
    new_user.set_password(password)
    new_user.save()

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




