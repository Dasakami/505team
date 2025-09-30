from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Testimonial, ContactMessage, TeamMember, BlogPost
from .forms import ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.management import call_command
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    return render(request, 'main/home.html', {
        'services': services,
        'testimonials': testimonials
    })

def about(request):
    return render(request, 'main/about.html')

def services(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'main/services.html', {'services': services})

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id, is_active=True)
    return render(request, 'main/service_detail.html', {'service': service})

def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'main/testimonials.html', {'testimonials': testimonials})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    services = Service.objects.filter(is_active=True)
    return render(request, 'main/contact.html', {'form': form, 'services': services})

def create_superuser(request):
    if not User.objects.filter(username="Dasakami").exists():
        User.objects.create_superuser("Dasakami", "dendasakami@gmail.com", "h72ivh-19")
        return HttpResponse("Суперпользователь создан!")
    else:
        return HttpResponse("Суперпользователь уже существует.")
    

def run_collectstatic(request):
    call_command('collectstatic', interactive=False, clear=True)
    return HttpResponse("Collectstatic выполнен!")

def yandex(request):
    return render(request, 'main/yandex_27aa4734362aa5ed.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)




def team(request):
    members = TeamMember.objects.filter(is_active=True)
    return render(request, 'team/team.html', {'members': members})

def member_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug, is_active=True)
    return render(request, 'team/member_detail.html', {'member': member})


def blog(request):
    posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/blog.html', {'page_obj': page_obj})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]
    
    return render(request, 'blog/detail.html', {
        'post': post,
        'related_posts': related_posts
    })