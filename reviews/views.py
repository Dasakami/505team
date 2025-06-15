from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Review
from .forms import ReviewForm

def reviews_list(request):
    """Список одобренных отзывов"""
    reviews = Review.objects.filter(status='approved').order_by('-created_at')
    paginator = Paginator(reviews, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'reviews/reviews_list.html', {'page_obj': page_obj})

def add_review(request):
    """Добавление нового отзыва"""
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Спасибо за ваш отзыв! Он будет опубликован после модерации.')
            return redirect('reviews_list')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form})