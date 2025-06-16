from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'

from django.views.static import serve
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Заменили url на re_path
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('sancho/', admin.site.urls),
    path('', include('main.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('team/', include('team.urls')),
    path('blog/', include('blog.urls')),
    path('reviews/', include('reviews.urls')),
    path('fun/', include('fun.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)