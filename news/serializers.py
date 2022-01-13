import re
from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = ["id","title","content"]

  def validate_title(self, title):
      if len(title)<3:
        raise serializers.ValidationError("3글자 이상!!")
      if not re.search(r"[ㄱ-힣]",title):
        raise serializers.ValidationError("한글을 써주세요.")
      return title

# # 비로그인 사용자용
# class NewsAnonymousSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = News
#     fields = ["id","title","content"]

# # 골드맵버쉽 사용자용
# class NewsGoldSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = News
#     fields = ["id","title","content","photo"]

# # 관리자용
# class NewsAdminSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = News
#     fields = ["id","title","content","photo","created_at","updated_at"]