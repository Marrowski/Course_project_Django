from django.core.signals import request_started
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import UserProfile, Category, Product, Photo, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import requests

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


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 100000)

    product_list = Product.objects.filter(
        category=category,
        price__gte=min_price,
        price__lte=max_price
    )
    context = {
        'category': category,
        'product_list': product_list
    }
    return render(request, 'main/product_list.html', context)



def product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    photos = product.photos.all()
    context = {
        'product': product,
        'photos': photos,
    }
    return render(request, 'main/product.html', context)


def get_or_create_cart(user):
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    else:
        return redirect('login')

def cart_add(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(user=request.user)
        quantity = int(request.POST.get('quantity', 1))

        CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        return JsonResponse({'message': 'Товар додано до кошика!'})
    return JsonResponse({'error': 'Некоректний запит'}, status=400)


def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_detail')


def cart_detail(request):
    cart = get_or_create_cart(request.user)
    return render(request, 'main/includes/cart.html', {'cart': cart})


def about_view(request):
    return render(request, 'main/about.html')

@login_required(login_url='login')
def delivery_order(request):

    cart = get_or_create_cart(request.user)


    api_key = '1f2a35c979752370bef1905edea9696d'
    api_url = 'https://api.novaposhta.ua/v2.0/json/'

    city_name = request.GET.get('city', '')
    data = []

    if city_name:
        payload = {
            "apiKey": api_key,
            "modelName": "Address",
            "calledMethod": "getWarehouses",
            "methodProperties": {
                "CityName": city_name
            }
        }

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            data_ap = response.json()
            data = data_ap.get('data', [])

    context = {
        'data': data,
        'city_name': city_name,
        'cart':cart
    }

    return render(request, 'main/delivery.html', context)

