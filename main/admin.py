from django.contrib import admin
from .models import Service, Testimonial, ContactMessage, BlogPost,  TeamMember, TeamMemberWork

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_from', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['client_name', 'client_company', 'text']
    list_editable = ['is_active']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at', 'service']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content', 'tags']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


class TeamMemberWorkInline(admin.TabularInline):
    model = TeamMemberWork
    extra = 1

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active', 'order']
    list_filter = ['is_active', 'position']
    search_fields = ['name', 'position', 'bio']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TeamMemberWorkInline]

@admin.register(TeamMemberWork)
class TeamMemberWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'member', 'created_at']
    list_filter = ['member', 'created_at']
    search_fields = ['title', 'description']