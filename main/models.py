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
    


class TeamMember(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    position = models.CharField(max_length=200, verbose_name='Должность')
    bio = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='team/', verbose_name='Фото', storage=MediaCloudinaryStorage())
    email = models.EmailField(verbose_name='Email', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', blank=True)
    instagram = models.CharField(max_length=100, verbose_name='Instagram', blank=True)
    vk = models.CharField(max_length=100, verbose_name='VK', blank=True)
    skills = models.TextField(verbose_name='Навыки', help_text='Через запятую')
    experience_years = models.IntegerField(verbose_name='Опыт (годы)', default=0)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    
    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'
        ordering = ['order']
    
    def __str__(self):
        return self.name
    
    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(',')]

class TeamMemberWork(models.Model):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='works', verbose_name='Участник')
    title = models.CharField(max_length=200, verbose_name='Название работы')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='team_works/', verbose_name='Изображение', storage=MediaCloudinaryStorage())
    url = models.URLField(verbose_name='Ссылка', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Работа участника'
        verbose_name_plural = 'Работы участников'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.member.name} - {self.title}'
    


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