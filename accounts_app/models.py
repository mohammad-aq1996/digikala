from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
from django.db import models
from django.utils.translation import gettext as _

class Users(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    receiver_name = models.CharField(verbose_name='Reciever Name', null=True, blank=True, max_length=50)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    post_id = models.CharField(max_length=10, null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    newsletter = models.BooleanField(default=False, null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


