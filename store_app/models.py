from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField


class Brand(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class MobileProduct(models.Model):
    STORAGE_CHOICE = (
        ('16', '16'),
        ('32', '32'),
        ('64', '64'),
        ('128', '128'),
        ('256', '256'),
        ('512', '512'),
    )
    SIMCARD_CHOICE = (
        ('1', 'تک سیمکارت'),
        ('2', 'دو سیمکارت'),
        ('4', 'چهار سیمکارت'),
    )
    NETWORK_CHOICE = (
        ('2G', '2G'),
        ('3G', '3G'),
        ('4G', '4G'),
        ('5G', '5G'),
    )
    persian_title = models.CharField(max_length=200)
    english_title = models.CharField(max_length=200)
    internal_storage = models.CharField(max_length=4, choices=STORAGE_CHOICE, default='256')
    image = models.ImageField(upload_to='store_app')
    networks = MultiSelectField(choices=NETWORK_CHOICE, default=['2G','3G', '4G'])
    pic_resolution = models.CharField(max_length=3, default='64')
    simcard_no = models.CharField(max_length=20, choices=SIMCARD_CHOICE, default='2')
    special_features = models.TextField()
    weight = models.CharField(max_length=4, default='225') 
    chipset = models.CharField(max_length=30, default='Apple A11 Bionic Chipset')    
    chipset_type = models.CharField(max_length=3, default='64')
    price = models.PositiveIntegerField(default=12000000)
    review = RichTextField()
    created = models.DateTimeField(auto_now_add=True) # jalali date
    updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, models.CASCADE, related_name='mobiles')
    category = models.ForeignKey(Category, models.CASCADE, related_name='mobiles')
    mobile_count = models.PositiveSmallIntegerField(default=2)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.english_title

    def get_absolute_url(self):
        return reverse('store_app:mobile-detail', kwargs={'pk': self.id})


class LaptopProduct(models.Model):
    STORAGE_CHOICE = (
        
        ('128', '128 گیگ'),
        ('256', '256 گیگ'),
        ('512', '512 گیگ'),
        ('1024', '1 ترابایت'),
        ('2048', '2 ترابایت'),
    )
    PORT_NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    RAM_CHOICE = (
        ('4', '4'),
        ('8', '8'),
        ('16', '16'),
        ('32', '32'),
    )
    persian_title = models.CharField(max_length=200)
    english_title = models.CharField(max_length=200)
    internal_storage = models.CharField(max_length=4, choices=STORAGE_CHOICE, default='256')
    image = models.ImageField(upload_to='store_app')
    screen_size = models.CharField(max_length=10, default='15.6 اینچ')
    usb_port_no = models.CharField(max_length=2, choices=PORT_NUMBER, default='3')
    ram = models.CharField(max_length=3, choices=RAM_CHOICE, default='16')
    weight = models.CharField(max_length=4, default='225')
    proccessor_serie = models.CharField(max_length=20, default='Core i7')    
    proccessor_builder = models.CharField(max_length=10, default='intel')
    graphic_proccessor_builder = models.CharField(max_length=10, default='NVIDIA')
    # lprice = models.CharField(max_length=10, default='20000000')
    price = models.PositiveIntegerField(default=20000000)
    review = RichTextField()
    created = models.DateTimeField(auto_now_add=True) # jalali date
    updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, models.CASCADE, related_name='laptops')
    category = models.ForeignKey(Category, models.CASCADE, related_name='laptops')
    laptop_count = models.PositiveSmallIntegerField(default=2)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.english_title

    def get_absolute_url(self):
        return reverse('store_app:laptop-detail', kwargs={'pk': self.id})


class Comment(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='d')
    product = models.ForeignKey(MobileProduct, models.CASCADE)

    def __str__(self):
        return self.status

class LaptopComment(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='d')
    product = models.ForeignKey(LaptopProduct, models.CASCADE)

    def __str__(self):
        return self.status


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(MobileProduct, models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
