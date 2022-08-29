from Tools.scripts.h2py import importable
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    phone = PhoneNumberField(null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'
