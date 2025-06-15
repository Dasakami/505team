from django.contrib import admin
from .models import TeamMember, TeamMemberWork

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