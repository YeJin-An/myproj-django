from django import forms
from shop.models import Review

class Reviewform(forms.ModelForm):
  class Meta:
    model = Review
    fields = "__all__"