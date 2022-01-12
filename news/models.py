from django.db import models

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class News(TimestampedModel):
  title = models.CharField(max_length=20, db_index = True)
  content = models.TextField()

