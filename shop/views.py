from rest_framework import viewsets
from shop.models import Review
from shop.forms import Reviewform
from django.urls import reverse_lazy
from shop.serializers import ReviewSerializer
from django.views.generic import ListView, CreateView

review_list = ListView.as_view(model=Review)
review_new = CreateView.as_view(model=Reviewform)

CreateView.as_view(
    model=Review, 
    form_class=Reviewform,
    success_url=reverse_lazy("shop:review_list")
)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer