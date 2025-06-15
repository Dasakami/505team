from django.contrib import admin
from .models import FunContent

@admin.register(FunContent)
class FunContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_type', 'is_featured', 'views_count', 'likes_count', 'created_at']
    list_filter = ['content_type', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    readonly_fields = ['views_count', 'likes_count', 'created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'content_type', 'is_featured')
        }),
        ('Медиа файлы', {
            'fields': ('image', 'video', 'video_url')
        }),
        ('Статистика', {
            'fields': ('views_count', 'likes_count', 'created_at'),
            'classes': ('collapse',)
        }),
    )