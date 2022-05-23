from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    receiver_name = models.CharField(verbose_name='Reciever Name', null=True, blank=True, max_length=50)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    post_id = models.CharField(max_length=10, null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    newsletter = models.BooleanField(default=False, null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
