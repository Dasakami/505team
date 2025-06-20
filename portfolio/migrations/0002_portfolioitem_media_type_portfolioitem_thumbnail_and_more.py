# Generated by Django 5.1.3 on 2025-06-15 10:46

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='media_type',
            field=models.CharField(choices=[('image', 'Изображение'), ('video', 'Видео'), ('both', 'Изображение и видео')], default='image', max_length=10, verbose_name='Тип медиа'),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='portfolio/thumbnails/', verbose_name='Превью для видео'),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='video',
            field=models.FileField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage, upload_to='portfolio/videos/', verbose_name='Видео файл'),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='video_url',
            field=models.URLField(blank=True, help_text='Если видео размещено на YouTube или Vimeo', verbose_name='Ссылка на видео (YouTube, Vimeo)'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(blank=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage, upload_to='portfolio/', verbose_name='Изображение'),
        ),
    ]
