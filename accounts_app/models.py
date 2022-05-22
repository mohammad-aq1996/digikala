from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    receiver_name = models.CharField(verbose_name='Reciever Name', max_length=50)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    post_id = models.CharField(max_length=10)
