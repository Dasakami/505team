from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Testimonial, ContactMessage
from .forms import ContactForm

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