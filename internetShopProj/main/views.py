from itertools import product

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import UserProfile, Category, Product, Photo

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request: HttpRequest):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'main/index.html', context)


def register(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone_number = request.POST.get('phone_number')
            context['email'] = email
            context['phone_number'] = phone_number
            if email and password and phone_number:
                try:
                    new_user = User.objects.create_user(username=email, email=email, password=password)
                    UserProfile.objects.create(phone=phone_number, user=new_user)
                    return redirect('login')
                except IntegrityError:
                    context['error'] = 'Користувач з такими даними вже зареєстрований'
            else:
                context['error'] = 'Будь ласка заповніть всі поля'

        return render(request, 'main/register.html', context)
    else:
        return redirect('index')


def auth(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email and password:
                user = authenticate(username=email, password=password)
                if user:
                    login(request,user)
                    return redirect('index')
                else:
                    context['error'] = "Неправильний email або пароль"
            else:
                context['error'] = "Заповніть будь ласка всі поля"
        return render(request, 'main/login.html', context)
    else:
        return redirect('index')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def product_view(request):
    product_list = Product.objects.prefetch_related('photos').all()
    context = {
        'product_list': product_list
    }
    return render(request, 'main/product_list.html', context)


def category_products(request,  category_id):
    category = Category.objects.get(id=category_id)
    product_list = Product.objects.filter(category=category)
    context = {
        'category': category,
        'product_list': product_list
    }
    return render(request, 'main/product_list.html', context)