from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from .forms import *

def admin_t(request):
    return render(request, 'admin_t.html')



def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    images = Image.objects.all()
    profiessionalchefs = Proffesionalchef.objects.all() 
    ourgallerys = Ourgallery.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'index.html', context={
        'categories': categories,
        'products': products,
        'images': images,
        'profiessionalchefs': profiessionalchefs,
        'ourgallerys': ourgallerys,
        'contacts': contacts,
    })




