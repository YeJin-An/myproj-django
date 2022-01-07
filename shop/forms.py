from django import forms
from shop.models import Review

class Reviewform(forms.ModelForm):
  class Meta:
    models = Review
    fields = "__all__"