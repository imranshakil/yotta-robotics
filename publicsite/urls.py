from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^services/', views.services, name='services'),
    url(r'^products/', views.products, name='products'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^contact/', views.contact, name='contact'),




]