from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('<slug:slug>/', views.member_detail, name='member_detail'),
]