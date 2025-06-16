from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static 
from .sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap(),
}


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path("create-superuser/", views.create_superuser),
    path('run/', views.run_collectstatic ),
    path('contact/', views.contact, name='contact'),
    path('yandex_27aa4734362aa5ed.html/', views.yandex, name='yandex_27aa4734362aa5ed'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)