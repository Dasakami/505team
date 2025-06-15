from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:item_id>/', views.portfolio_detail, name='portfolio_detail'),
]