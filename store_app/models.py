from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    persian_title = models.CharField(max_length=200)
    english_title = models.CharField(max_length=200)
    internal_storage = models.CharField(max_length=4, default=256)
    image = models.ImageField(upload_to='store_app')
    networks = models.CharField(max_length=10, default='2G,3G,4G')
    pic_resolution = models.CharField(max_length=3, default='64')
    simcard_no = models.CharField(max_length=20, default='تک سیمکارت')
    special_features = models.CharField(max_length=300)
    weight = models.CharField(max_length=4, default='225') 
    chipset = models.CharField(max_length=30, default='Apple A11 Bionic Chipset')    
    chipset_type = models.CharField(max_length=3, default='64')
    price = models.CharField(max_length=10, default='12000000')
    review = models.TextField() # ckeditor
    created = models.DateTimeField(auto_now_add=True) # jalali date
    updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, models.CASCADE, related_name='mobiles')
    category = models.ForeignKey(Category, models.CASCADE, related_name='mobiles')

    def __str__(self):
        return self.persian_title

    def get_absolute_url(self):
        return reverse('store_app:mobile-detail', kwargs={'pk': self.id})


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


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(MobileProduct, models.CASCADE)
