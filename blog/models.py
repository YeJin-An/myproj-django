from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=20, db_index = True)
  content = models.TextField()

