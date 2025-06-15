from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'rating', 'status', 'service_used', 'created_at']
    list_filter = ['status', 'rating', 'would_recommend', 'created_at']
    search_fields = ['name', 'email', 'company', 'title', 'text']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Информация о клиенте', {
            'fields': ('name', 'email', 'company', 'avatar')
        }),
        ('Отзыв', {
            'fields': ('title', 'text', 'rating', 'service_used', 'would_recommend')
        }),
        ('Модерация', {
            'fields': ('status', 'admin_comment')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_reviews', 'reject_reviews']
    
    def approve_reviews(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f'{updated} отзывов одобрено.')
    approve_reviews.short_description = 'Одобрить выбранные отзывы'
    
    def reject_reviews(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} отзывов отклонено.')
    reject_reviews.short_description = 'Отклонить выбранные отзывы'