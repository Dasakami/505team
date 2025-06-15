from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    short_description = models.CharField(max_length=300, verbose_name='Краткое описание')
    icon = models.CharField(max_length=50, verbose_name='Иконка', help_text='Название иконки из Lucide')
    price_from = models.IntegerField(verbose_name='Цена от', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=200, verbose_name='Имя клиента')
    client_company = models.CharField(max_length=200, verbose_name='Компания', blank=True)
    client_avatar = models.ImageField(upload_to='testimonials/', verbose_name='Аватар', blank=True,storage=MediaCloudinaryStorage()) 
    text = models.TextField(verbose_name='Отзыв')
    rating = models.IntegerField(verbose_name='Рейтинг', choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.client_name} - {self.rating}★'

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Услуга')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.email}'