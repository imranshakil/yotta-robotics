from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'login', views.login, name='login'),
    url(r'rgistration', views.rgistration, name='rgistration'),
    url(r'PasswordChange', views.PasswordChange, name='PasswordChange'),
    url(r'EmailTest', views.EmailTest, name='EmailTest'),
    url(r'UserCheck', views.UserCheck, name='UserCheck'),
    url(r'ProfileUpdate', views.ProfileUpdate, name='ProfileUpdate'),
]