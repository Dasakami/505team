from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import FunContent

def fun_list(request):
    """Список смешного контента"""
    content_type = request.GET.get('type', 'all')
    
    if content_type == 'all':
        content = FunContent.objects.all()
    else:
        content = FunContent.objects.filter(content_type=content_type)
    
    paginator = Paginator(content, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'fun/fun_list.html', {
        'page_obj': page_obj,
        'active_type': content_type
    })

def fun_detail_json(request, pk):
    """AJAX: данные для модального окна"""
    content = get_object_or_404(FunContent, pk=pk)
    content.increment_views()

    return JsonResponse({
        'title': content.title,
        'description': content.description,
        'created_at': content.created_at.strftime('%d.%m.%Y'),
        'likes': content.likes_count,
        'views': content.views_count,
        'type': content.content_type,
        'video_url': content.video.url if content.video else '',
        'image_url': content.image.url if content.image else '',
    })

def like_content(request, pk):
    """AJAX лайк"""
    if request.method == 'POST':
        content = get_object_or_404(FunContent, pk=pk)
        content.likes_count += 1
        content.save(update_fields=['likes_count'])
        return JsonResponse({'likes': content.likes_count})
    return JsonResponse({'error': 'Invalid request'})
