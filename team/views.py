from django.shortcuts import render, get_object_or_404
from .models import TeamMember

def team(request):
    members = TeamMember.objects.filter(is_active=True)
    return render(request, 'team/team.html', {'members': members})

def member_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug, is_active=True)
    return render(request, 'team/member_detail.html', {'member': member})