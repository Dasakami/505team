from rest_framework import serializers
from .models import PortfolioItem, PortfolioCategory


class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']


class PortfolioItemSerializer(serializers.ModelSerializer):
    category = PortfolioCategorySerializer(read_only=True)
    category_slug = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=PortfolioCategory.objects.all(),
        source='category',
        write_only=True,
        required=False
    )
    main_image = serializers.SerializerMethodField()
    youtube_embed_url = serializers.SerializerMethodField()
    
    class Meta:
        model = PortfolioItem
        fields = [
            'id',
            'title',
            'description',
            'category',
            'category_slug',
            'media_type',
            'image',
            'video',
            'video_url',
            'thumbnail',
            'url',
            'client',
            'technologies',
            'is_featured',
            'created_at',
            'main_image',
            'youtube_embed_url',
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_main_image(self, obj):
        image = obj.get_main_image()
        return image.url if image else None
    
    def get_youtube_embed_url(self, obj):
        return obj.get_youtube_embed_url()

