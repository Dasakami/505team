from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.views.static import serve
handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('sancho/', admin.site.urls),
    path('', include('main.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('reviews/', include('reviews.urls')),
    path('fun/', include('fun.urls')),
    path('api/', include('main.api_urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)