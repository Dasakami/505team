from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_list, name='fun_list'),
    path('<int:pk>/json/', views.fun_detail_json, name='fun_detail_json'),
    path('<int:pk>/like/', views.like_content, name='like_content'),
]
