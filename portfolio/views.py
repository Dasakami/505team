from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import PortfolioItem, PortfolioCategory
from .serializers import PortfolioItemSerializer, PortfolioCategorySerializer


class PortfolioCategoryListAPIView(generics.ListAPIView):
    queryset = PortfolioCategory.objects.all()
    serializer_class = PortfolioCategorySerializer
    permission_classes = [permissions.AllowAny]


class PortfolioItemListAPIView(generics.ListAPIView):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'is_featured', 'media_type']
    
    def get_queryset(self):
        queryset = PortfolioItem.objects.all()
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset


class PortfolioItemDetailAPIView(generics.RetrieveAPIView):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        item = self.get_object()
        context['related_items'] = PortfolioItem.objects.filter(
            category=item.category
        ).exclude(id=item.id)[:3]
        return context
