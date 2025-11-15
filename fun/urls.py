from django.urls import path
from .views import FunContentListAPIView, FunContentDetailAPIView, like_content

urlpatterns = [
    path('', FunContentListAPIView.as_view(), name='fun-list'),
    path('<int:pk>/', FunContentDetailAPIView.as_view(), name='fun-detail'),
    path('<int:pk>/like/', like_content, name='fun-like'),
]
