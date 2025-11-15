from django.urls import path
from .api_views import (
    ContactMessageView,
    TeamMemberListView,
    TeamMemberDetailView,
    BlogPostListAPIView,
    BlogPostDetailAPIView,
    ServiceListAPIView,
    ServiceDetailAPIView,
    TestimonialListAPIView,
)

urlpatterns = [
    path('contact/', ContactMessageView.as_view(), name='contact-message'),
    path('team/', TeamMemberListView.as_view(), name='team-list'),
    path('team/<slug:slug>/', TeamMemberDetailView.as_view(), name='team-detail'),
    path('blog/', BlogPostListAPIView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', BlogPostDetailAPIView.as_view(), name='blog-detail'),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:id>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
]
