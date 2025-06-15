from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'
    
    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='portfolio/', verbose_name='Изображение', storage=MediaCloudinaryStorage())
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