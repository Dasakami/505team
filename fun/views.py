from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import FunContent
from .serializers import FunContentSerializer


class FunContentListAPIView(generics.ListAPIView):
    queryset = FunContent.objects.all()
    serializer_class = FunContentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['content_type', 'is_featured']
    
    def get_queryset(self):
        queryset = FunContent.objects.all()
        content_type = self.request.query_params.get('type', None)
        if content_type and content_type != 'all':
            queryset = queryset.filter(content_type=content_type)
        return queryset


class FunContentDetailAPIView(generics.RetrieveAPIView):
    queryset = FunContent.objects.all()
    serializer_class = FunContentSerializer
    permission_classes = [permissions.AllowAny]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increment_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def like_content(request, pk):
    try:
        content = FunContent.objects.get(pk=pk)
        content.likes_count += 1
        content.save(update_fields=['likes_count'])
        return Response({'likes': content.likes_count}, status=status.HTTP_200_OK)
    except FunContent.DoesNotExist:
        return Response({'error': 'Content not found'}, status=status.HTTP_404_NOT_FOUND)
