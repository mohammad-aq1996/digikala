from django.db import models
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
    image = models.ImageField(upload_to='store_app')
    english_title = models.CharField(max_length=200)
    networks = models.CharField(max_length=10, default='2G,3G,4G')
    pic_resolution = models.CharField(max_length=15, default='64 مگاپیکسل')
    simcard_no = models.CharField(max_length=20, default='تک سیمکارت')
    special_features = models.CharField(max_length=300)
    weight = models.CharField(max_length=10, default='225 گرم') 
    chipset = models.CharField(max_length=30, default='Apple A11 Bionic Chipset')    
    chipset_type = models.CharField(max_length=15, default='64 بیت')
    review = models.TextField() # ckeditor
    created = models.DateTimeField(auto_now_add=True) # jalali date
    updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, models.CASCADE, related_name='mobiles')
    category = models.ForeignKey(Category, models.CASCADE, related_name='mobiles')

    def __str__(self):
        return self.persian_title

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.id})


class Comment(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS)
    product = models.ForeignKey(MobileProduct, models.CASCADE)

    def __str__(self):
        return self.status