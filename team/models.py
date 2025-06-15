from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

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