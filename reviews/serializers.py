from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'name',
            'email',
            'company',
            'avatar',
            'rating',
            'title',
            'text',
            'service_used',
            'would_recommend',
            'status',
            'admin_comment',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'status', 'admin_comment', 'created_at', 'updated_at']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'name',
            'email',
            'company',
            'avatar',
            'rating',
            'title',
            'text',
            'service_used',
            'would_recommend',
        ]

