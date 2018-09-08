from django.http import request
from django.db import connection
import hashlib, os
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format


class common:

    def moduleName(self):
        rf = request.GET.rf
        return rf

    # Array count
    def ObjectCount(self,object):
        cc = 0
        for row in object:
            cc = cc + 1

        return cc

    #Password Create
    def PasswordGenerate(self,password):
        newpass = 'DbCDKL'+password+'ZoomPay100'
        password_hash = hashlib.sha256(newpass.encode('utf-8')).hexdigest()
        return password_hash

    #todays date
    def dateToday(self):
        dt = datetime.now()
        df = DateFormat(dt)
        today = df.format('Y-m-d')
        return today

    def dateTodayInt(self):
        dt = datetime.now()
        df = DateFormat(dt)
        today = df.format('Ymd')
        return today

    #customer ID Generate
    def CusotmerIDGen(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM customers_info ")
        rows = cursor.fetchall()
        count = self.ObjectCount(self, rows)
        cl = count + 1
        #get todays Int date
        customerID = str(self.dateTodayInt(self)) + str(cl)

        return customerID

