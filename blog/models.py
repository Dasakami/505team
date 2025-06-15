from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержание')
    excerpt = models.TextField(max_length=300, verbose_name='Краткое описание')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', storage=MediaCloudinaryStorage())
    author = models.CharField(max_length=100, verbose_name='Автор')
    tags = models.CharField(max_length=200, verbose_name='Теги', blank=True, help_text='Через запятую')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]