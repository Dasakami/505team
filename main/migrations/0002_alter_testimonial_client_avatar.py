# Generated by Django 5.1.3 on 2025-06-15 10:46

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client_avatar',
            field=models.ImageField(blank=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='testimonials/', verbose_name='Аватар'),
        ),
    ]
