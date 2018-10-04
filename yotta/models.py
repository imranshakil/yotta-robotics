
# Create your models here.
from datetime import date
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=80)
    phone = models.IntegerField(max_length=18)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    country = CountryField()
    city = models.CharField("City",max_length=1024)
    address1 = models.CharField("Address line 1",max_length=1024)
    address2 = models.CharField("Address line 2",max_length=1024)
    academy = models.CharField("If valid", max_length=512)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    social_profile = models.CharField(max_length=256)
    website = models.URLField(max_length=200, blank=False)


