from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def page_not_found(request, exception=None):
    return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def server_error(request):
    return Response({'error': 'Server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
