"""
URL configuration for internetShopProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import (index, register, auth, logout_view, product_view, category_products,
                        product_page, cart_add, cart_remove, cart_detail, about_view, delivery_order)

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path(, index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth, name='login'),
    path('logout', logout_view, name='logout'),
    path('products/', product_view, name='products'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_page, name='product'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),
    path('about/', about_view, name='about'),
    path('order/', delivery_order, name='delivery')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
