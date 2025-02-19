"""
URL configuration for homework_shop project.

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

from main.views import main_page
from main.views import computers_category
from main.views import smartphones_category
from main.views import audiotech_category
from main.views import components_category
from main.views import household_category
from main.views import vinga_page
from main.views import asus_page
from main.views import lenovo_page
from main.views import acer_page
from main.views import redmi_page
from main.views import samsung_page
from main.views import motorola_page
from main.views import apple_page
from main.views import jbl_page
from main.views import vinga_headphones
from main.views import genius_page
from main.views import trust_page
from main.views import nvidia_page
from main.views import intel_page
from main.views import matplat_page
from main.views import kingston_page
from main.views import landuary_page
from main.views import indesit_page
from main.views import fridge_page
from main.views import dahati_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_page, name='main'),
    path('computers/', computers_category, name='computers'),
    path('smartphones/', smartphones_category, name='smartphones'),
    path('audiotech/', audiotech_category, name='audio'),
    path('components/', components_category, name='components'),
    path('household/', household_category, name='house'),
    path('vinga/', vinga_page, name='vinga'),
    path('asus/', asus_page, name='asus'),
    path('lenovo/', lenovo_page, name='lenovo'),
    path('acer/', acer_page, name='acer'),
    path('redmi/', redmi_page, name='redmi'),
    path('samsung/', samsung_page, name='samsung'),
    path('motorola/', motorola_page, name='motorola'),
    path('apple/', apple_page, name='apple'),
    path('jbl/', jbl_page, name='jbl'),
    path('vinga_head/', vinga_headphones, name='vinga_a'),
    path('genius/', genius_page, name='genius'),
    path('trust/', trust_page, name='trust'),
    path('nvidia', nvidia_page, name='nvidia'),
    path('intel/', intel_page, name='intel'),
    path('mat/', matplat_page, name='tuf'),
    path('kingston/', kingston_page, name='kingston'),
    path('landuary/', landuary_page, name='lan'),
    path('indesit/', indesit_page, name='indesit'),
    path('bosch/', fridge_page, name='bosch'),
    path('dahati/', dahati_page, name='dahati')
]
