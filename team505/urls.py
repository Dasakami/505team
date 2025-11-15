from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sancho/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/fun/', include('fun.urls')),
]

# Только для медиа файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
