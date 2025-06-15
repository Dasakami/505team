from django.db import models

class FunContent(models.Model):
    CONTENT_TYPES = [
        ('image', 'Изображение'),
        ('video', 'Видео'),
        ('gif', 'GIF'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES, verbose_name='Тип контента')
    
    # Медиа файлы
    image = models.ImageField(upload_to='fun/images/', verbose_name='Изображение', blank=True)
    video = models.FileField(upload_to='fun/videos/', verbose_name='Видео файл', blank=True)
    video_url = models.URLField(verbose_name='Ссылка на видео', blank=True)
    
    # Дополнительные поля
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемое')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='Лайки')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Смешной контент'
        verbose_name_plural = 'Смешной контент'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_main_media(self):
        """Возвращает главный медиа файл"""
        if self.content_type == 'image' and self.image:
            return self.image
        elif self.content_type in ['video', 'gif'] and self.video:
            return self.video
        return None
    
    def increment_views(self):
        """Увеличивает счетчик просмотров"""
        self.views_count += 1
        self.save(update_fields=['views_count'])