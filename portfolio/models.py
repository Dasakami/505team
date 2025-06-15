from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage, VideoMediaCloudinaryStorage
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'
    
    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    MEDIA_TYPES = [
        ('image', 'Изображение'),
        ('video', 'Видео'),
        ('both', 'Изображение и видео'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, verbose_name='Категория')
    
    # Медиа файлы
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image', verbose_name='Тип медиа')
    image = models.ImageField(upload_to='portfolio/', verbose_name='Изображение', blank=True, storage=MediaCloudinaryStorage)
    video = models.FileField(upload_to='portfolio/videos/', verbose_name='Видео файл', blank=True, storage=VideoMediaCloudinaryStorage)
    video_url = models.URLField(verbose_name='Ссылка на видео (YouTube, Vimeo)', blank=True, help_text='Если видео размещено на YouTube или Vimeo')
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/', verbose_name='Превью для видео', blank=True)
    
    url = models.URLField(verbose_name='Ссылка', blank=True)
    client = models.CharField(max_length=200, verbose_name='Клиент', blank=True)
    technologies = models.CharField(max_length=500, verbose_name='Технологии', blank=True)
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Работа портфолио'
        verbose_name_plural = 'Работы портфолио'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_main_image(self):
        """Возвращает главное изображение (обложку или превью)"""
        if self.thumbnail:
            return self.thumbnail
        elif self.image:
            return self.image
        return None
    
    def get_youtube_embed_url(self):
        """Преобразует YouTube ссылку в embed формат"""
        if 'youtube.com/watch?v=' in self.video_url:
            video_id = self.video_url.split('watch?v=')[1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'youtu.be/' in self.video_url:
            video_id = self.video_url.split('youtu.be/')[1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return self.video_url