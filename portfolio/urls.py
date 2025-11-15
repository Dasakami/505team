from django.urls import path
from .views import (
    PortfolioCategoryListAPIView,
    PortfolioItemListAPIView,
    PortfolioItemDetailAPIView
)

urlpatterns = [
    path('categories/', PortfolioCategoryListAPIView.as_view(), name='portfolio-categories'),
    path('', PortfolioItemListAPIView.as_view(), name='portfolio-list'),
    path('<int:id>/', PortfolioItemDetailAPIView.as_view(), name='portfolio-detail'),
]
