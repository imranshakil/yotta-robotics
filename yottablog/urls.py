"""YottaRobotics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include

from yottablog import views

urlpatterns = [
    #path('', views.home, name='home'),
    url(r'^blog_main/', views.blog_main, name='blog_main'),
    url(r'^blog_header/', views.blog_header, name='blog_header'),

    #Blog site url only
    #url(r'^blog_menu', views.blog_menu, name='blog_menu'),
    #url(r'^highlight', views.highlight, name='highlight'),
    #url(r'^public_news_feed', views.public_news_feed, name='public_news_feed'),
]
