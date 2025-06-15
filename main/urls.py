from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path("create-superuser/", views.create_superuser),
    path('contact/', views.contact, name='contact'),
]