from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=255)
    favicon  = models.ImageField(upload_to='media/favicon')
    logo = models.ImageField(upload_to='media/logo')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/team')
    position = models.CharField(max_length=255)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Services(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/services')
    iconlink = models.CharField(max_length=100,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Menu(models.Model):
    COFFEE = (
        ('Hot Coffee','Hot Coffee'),
        ('Cold Coffee','Cold Coffee')

        )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/menu')
    category  = models.CharField(max_length=100, choices=COFFEE,null=True)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(null=True, region='NP')
    date = models.DateField()
    time = models.TimeField()
    number_of_guest = models.IntegerField(max_length=10)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.time} / {self.date}"

class Client(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/client')
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(null=True,blank=True, region='NP')
    message = models.TextField()
    profession = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.profession}"






