from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        user = self.request.query_params.get('user')
        email = self.request.query_params.get('email')
        # queryset = User.objects.raw("SELECT * From auth_user where username= %s and email= %s ",[user,email])
        queryset = User.objects.raw("SELECT * From auth_user where username= %s and email= %s ",[user,email])
        return queryset

class UserLoginListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        userid = self.request.POST.get('userid'),
        email = self.request.POST.get('email')
        # print(email)
        # queryset = User.objects.raw("SELECT * From auth_user where username= %s and email= %s ",[user,email])
        queryset = User.objects.raw("SELECT * From auth_user where username= %s and email= %s ", [userid, email])
        #print(userid)
        return Response(queryset)


class TokenCreate(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        # user = self.request.POST.get('user')
        user = self.request.query_params.get('user')
        token = Token.objects.create(user = user)
        return token