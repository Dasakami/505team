from rest_framework import serializers
from .models import FunContent


class FunContentSerializer(serializers.ModelSerializer):
    main_media = serializers.SerializerMethodField()
    
    class Meta:
        model = FunContent
        fields = [
            'id',
            'title',
            'description',
            'content_type',
            'image',
            'video',
            'video_url',
            'is_featured',
            'views_count',
            'likes_count',
            'created_at',
            'main_media',
        ]
        read_only_fields = ['id', 'views_count', 'likes_count', 'created_at']
    
    def get_main_media(self, obj):
        media = obj.get_main_media()
        return media.url if media else None

