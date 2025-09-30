from rest_framework import generics, permissions, status
from .models import Service, Testimonial, TeamMember, BlogPost

from .serializers import (
    ServiceSerializer, ContactMessageSerializer, TeamMemberSerializer,  TestimonialSerializer, BlogPostSerializer
)

class ContactMessageView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer

class TeamMemberDetailView(generics.RetrieveAPIView):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    lookup_field = 'slug'

class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer

class BlogPostDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        post = self.get_object()
        context['related_posts'] = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]
        return context
    
class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = 'id'

class TestimonialListAPIView(generics.ListAPIView):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer