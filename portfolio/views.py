from django.shortcuts import render, get_object_or_404
from .models import PortfolioItem, PortfolioCategory

def portfolio(request):
    category_slug = request.GET.get('category')
    categories = PortfolioCategory.objects.all()
    
    if category_slug:
        category = get_object_or_404(PortfolioCategory, slug=category_slug)
        items = PortfolioItem.objects.filter(category=category)
    else:
        items = PortfolioItem.objects.all()
        category = None
    
    return render(request, 'portfolio/portfolio.html', {
        'items': items,
        'categories': categories,
        'active_category': category
    })

def portfolio_detail(request, item_id):
    item = get_object_or_404(PortfolioItem, id=item_id)
    related_items = PortfolioItem.objects.filter(category=item.category).exclude(id=item.id)[:3]
    
    return render(request, 'portfolio/detail.html', {
        'item': item,
        'related_items': related_items
    })