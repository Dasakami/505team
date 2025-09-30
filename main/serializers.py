from rest_framework import serializers
from .models import Service, Testimonial, ContactMessage, TeamMember, TeamMemberWork, BlogPost

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "short_description",
            "icon",
            "price_from",
            "is_active",
            "order",
        ]
        read_only_fields = ["id"]

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            "id",
            "client_name",
            "client_company",
            "client_avatar",
            "text",
            "rating",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class ContactMessageSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        slug_field="name", queryset=Service.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "service",
            "message",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["id", "created_at", "is_read"]


class TeamMemberWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberWork
        fields = [
            "id",
            "title",
            "description",
            "image",
            "url",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

class TeamMemberSerializer(serializers.ModelSerializer):
    works = TeamMemberWorkSerializer(many=True, read_only=True)
    skills = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = [
            "id",
            "name",
            "slug",
            "position",
            "bio",
            "photo",
            "email",
            "phone",
            "telegram",
            "instagram",
            "vk",
            "skills",
            "experience_years",
            "is_active",
            "order",
            "works",
        ]
        read_only_fields = ["id", "works"]

    def get_skills(self, obj):
        return obj.get_skills_list()


class BlogPostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "excerpt",
            "image",
            "author",
            "tags",
            "is_published",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_tags(self, obj):
        return obj.get_tags_list()
