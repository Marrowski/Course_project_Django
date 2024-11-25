"""
URL configuration for homework03 project.

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

from main.views import list_show
from main.views import star_wars
from main.views import luke_skywalker
from main.views import leya_organa, han_solo
from main.views import output_file

from main.views import json_response, html_response, text_response
from main.views import priority_page

from main.views import names_page
from main.views import questions_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_show),
    path('main/', star_wars),
    path('luke/', luke_skywalker, name='luke'),
    path('leya/', leya_organa, name='leya'),
    path('han/', han_solo, name='han'),
    path('output/', output_file),
    path('jsonfile/', json_response),
    path('htmlfile/', html_response),
    path('textfile/', text_response),
    path('priority/', priority_page),
    path('sorting_names/', names_page),
    path('questions/', questions_page)
]
