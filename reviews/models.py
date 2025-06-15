from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На модерации'),
        ('approved', 'Одобрен'),
        ('rejected', 'Отклонен'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    company = models.CharField(max_length=200, verbose_name='Компания', blank=True)
    avatar = models.ImageField(upload_to='reviews/avatars/', verbose_name='Аватар', blank=True)
    
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='От 1 до 5 звезд'
    )
    
    title = models.CharField(max_length=200, verbose_name='Заголовок отзыва')
    text = models.TextField(verbose_name='Текст отзыва')
    
    # Дополнительные поля
    service_used = models.CharField(max_length=200, verbose_name='Какую услугу использовали', blank=True)
    would_recommend = models.BooleanField(default=True, verbose_name='Рекомендуете ли нас?')
    
    # Модерация
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    admin_comment = models.TextField(verbose_name='Комментарий администратора', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.rating}★ ({self.get_status_display()})'