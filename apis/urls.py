from django.conf.urls import url
from apis import views

urlpatterns = [
    url(r'^$', views.UserListView.as_view()),
    url(r'login', views.UserLoginListView.as_view()),
    url(r'getToken', views.TokenCreate.as_view()),
]