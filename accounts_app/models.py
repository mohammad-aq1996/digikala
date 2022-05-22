from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    receiver_name = models.CharField(verbose_name='Reciever Name', null=True, blank=True, max_length=50)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    post_id = models.CharField(max_length=10, null=True, blank=True)
