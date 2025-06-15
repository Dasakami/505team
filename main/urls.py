from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path("create-superuser/", views.create_superuser),
    path('run/', views.run_collectstatic ),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)