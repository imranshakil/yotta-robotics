import json

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.conf.urls import url

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.db import connection
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from classes.db.db import DB
from classes.common import common
from django.core.mail import send_mail

import base64
from django.core.files.base import ContentFile
import tempfile
import shutil

FILE_UPLOAD_DIR = 'static/uploader/user'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def login(request):
    userid = request.POST.get('userid'),
    password = request.POST.get('password')
    # sql = ("SELECT id,username,email FROM auth_user where username= %s and password=%s ", [userid, password])
    # result = DB.Query(sql)
    genPass = common.PasswordGenerate(common,password)

    cursor = connection.cursor()
    cursor.execute("SELECT id,customer_id,type,name,phone,email,userid,status,address FROM customers_info where userid= %s and password=%s and status=1 ", [userid, genPass])
    rows = cursor.fetchall()
    count = common.ObjectCount(common,rows)

    if count >0:
        result = []
        columns = [col[0] for col in cursor.description]
        for row in rows:
            result.append(dict(zip(columns, row)))
        json_data = json.dumps(result)
        data_sent = '{"status":"1","desc":"Authentication Success","UserData":'+json_data+'}'
        return HttpResponse(data_sent, content_type="application/json")
    else:
        json_data = '{"status":"0","desc":"Invalid Login Credential"}'
        return HttpResponse(json_data, content_type="application/json")


def Authenticate(userid,password):

    genPass = common.PasswordGenerate(common,password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers_info where userid= %s and password=%s and status=1 ", [userid, genPass])
    rows = cursor.fetchall()
    count = common.ObjectCount(common,rows)

    if count == 1:
        return 1
    else:
        return 0


@csrf_exempt
def rgistration(request):
    userid = request.POST.get('userid'),
    password = request.POST.get('password')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    status = 1
    type = 'Individual'
    passd = common.PasswordGenerate(common,password)
    # print(email)
    customer_id = common.CusotmerIDGen(common)
    # print(customer_id)

    if(str(userid) == ''):
        json_data = '{"status":"211","desc":"Userid can not be empty"}'
        return HttpResponse(json_data, content_type="application/json")
    elif (str(email) == ''):
        json_data = '{"status":"211","desc":"Email can not be empty"}'
        return HttpResponse(json_data, content_type="application/json")
    elif (str(name) == ''):
        json_data = '{"status":"211","desc":"Name can not be empty"}'
        return HttpResponse(json_data, content_type="application/json")
    elif (str(password) == ''):
        json_data = '{"status":"211","desc":"Password can not be empty"}'
        return HttpResponse(json_data, content_type="application/json")
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT id,userid,email FROM customers_info where userid= %s OR email =%s ", [userid, email])
        rows = cursor.fetchall()
        count = common.ObjectCount(common, rows)
        if count > 0:
            json_data = '{"status":"3","desc":"Email or username already exist, plesse try with different email or username"}'
            return HttpResponse(json_data, content_type="application/json")
        else:
            insert = cursor.execute(
                " INSERT INTO customers_info (customer_id,type,name,phone,email,userid,password,status) Values (%s,%s,%s,%s,%s,%s,%s,%s) ",
                [customer_id, type, name, phone, email, userid, passd, status])
            if (insert):
                json_data = '{"status":"1","desc":"Successfully Registered"}'
                return HttpResponse(json_data, content_type="application/json")
            else:
                json_data = '{"status":"0","desc":"Email or username already exist, plesse try with different email or username"}'
                return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def ProfileUpdate(request):
    userid = request.POST.get('uid'),
    password = request.POST.get('pwd')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    photo = request.POST.get('photo')

    if Authenticate(userid, password) == 1:

        if(str(userid) == ''):
            json_data = '{"status":"211","desc":"Userid can not be empty"}'
            return HttpResponse(json_data, content_type="application/json")
        elif (str(email) == ''):
            json_data = '{"status":"211","desc":"Email can not be empty"}'
            return HttpResponse(json_data, content_type="application/json")
        else:
            cursor = connection.cursor()
            cursor.execute("SELECT id,userid,email FROM customers_info where userid= %s ", [userid])
            rows = cursor.fetchall()
            count = common.ObjectCount(common, rows)
            if count > 0:

                DataImageToFile(photo,userid)

                insert = cursor.execute(
                    " Update customers_info SET phone=%s,email=%s, address=%s WHERE userid =%s ",[phone, email, address,userid])
                if (insert):
                    json_data = '{"status":"1","desc":"Successfully Updated"}'
                    return HttpResponse(json_data, content_type="application/json")
                else:
                    json_data = '{"status":"0","desc":"Failed to update"}'
                    return HttpResponse(json_data, content_type="application/json")
            else:
                json_data = '{"status":"3","desc":"Failed to updated"}'
                return HttpResponse(json_data, content_type="application/json")
    else :
        json_data = '{"status":"0","desc":"Invalid Authentication"}'
        return HttpResponse(json_data, content_type="application/json")



def EmailTest(self):
    send_mail('Welcome to Zoom Pay','Test Email','zoompay@datalibrary.io',['shopno@ymail.com',])


@csrf_exempt
def PasswordChange(request):
    userid = request.POST.get('userid'),
    password = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')

    if Authenticate(userid,password) ==1 :

        genPass = common.PasswordGenerate(common, newpassword)

        cursor = connection.cursor()
        update = cursor.execute("UPDATE customers_info SET password=%s where userid=%s ", [genPass, userid])


        if update :
            data_sent = '{"status":"1","desc":"Successfully Changed your password"}'
            return HttpResponse(data_sent, content_type="application/json")
        else:
            json_data = '{"status":"0","desc":"Failed to change your password"}'
            return HttpResponse(json_data, content_type="application/json")
    else:
        json_data = '{"status":"0","desc":"Invalid Authentication"}'
        return HttpResponse(json_data, content_type="application/json")


def PaymentIN(request):
    #Payment In
    pass


def UserCheck(request):
    userid = request.POST.get('userid'),
    password = request.POST.get('password')
    customer_id = request.POST.get('cis')

    if Authenticate(userid, password) == 1:

        cursor = connection.cursor()
        cursor.execute("SELECT id,userid,email FROM customers_info where userid= %s ", [userid])
        rows = cursor.fetchall()
        count = common.ObjectCount(common, rows)

        if count >0:
            result = []
            columns = [col[0] for col in cursor.description]
            for row in rows:
                result.append(dict(zip(columns, row)))
            json_data = json.dumps(result)
            data_sent = '{"status":"1","desc":"Successfully Changed your password","userData": '+json_data+'}'
            return HttpResponse(data_sent, content_type="application/json")
        else:
            json_data = '{"status":"0","desc":"Failed to change your password"}'
            return HttpResponse(json_data, content_type="application/json")
    else:
        json_data = '{"status":"0","desc":"Invalid Authentication"}'
        return HttpResponse(json_data, content_type="application/json")


def DataImageToFile(data,filename):
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    dataImage = ContentFile(base64.b64decode(imgstr), name=str(filename)+'.png')  # You can save this as file instance.
    fd, filepath = tempfile.mkstemp(prefix=(dataImage.name), dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(dataImage, dest)
    return filepath


class SettingsBackend:
    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
