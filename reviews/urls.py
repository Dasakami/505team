from django.urls import path
from .views import ReviewListAPIView, ReviewCreateAPIView

urlpatterns = [
    path('', ReviewListAPIView.as_view(), name='reviews-list'),
    path('add/', ReviewCreateAPIView.as_view(), name='review-create'),
]
