from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
        abstract = True

class News(TimestampedModel):
  title = models.CharField(max_length=20, db_index = True),
                            validators=[
                              MinLengthValidator(3, message),
                              RegexValidator(r"[ㄱ-힝]", message="한글을 입력해주세요.")
                            ])

  content = models.TextField()
  photo = models.ImageField(blank = True)

