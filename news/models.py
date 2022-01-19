from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
        abstract = True

class News(TimestampedModel):
  title = models.CharField(max_length=20, db_index = True)
  content = models.TextField()
  photo = models.ImageField(blank = True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

