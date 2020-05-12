from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Review(models.Model):

    details = models.TextField()
    Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'))
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    date = models.DateTimeField(default=timezone.now)
    Product_CHOICES = (
    (1, 'SmartPhones'),
    (2, 'Smart Watches'),
    (3, 'Smart TVs'))
    products = models.IntegerField(choices=Product_CHOICES, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.details
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    cost = models.IntegerField(default=0)
    Category_CHOICES = (
        (1, 'SmartPhones'),
        (2, 'Smart Watches'),
        (3, 'Smart TVs'))
    categories = models.IntegerField(choices=Category_CHOICES, default=0)
    release_date = models.DateField(max_length=8)
    description = models.TextField()
    image = models.ImageField(default='example.jpg', upload_to='media')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product-description', kwargs={'pk': self.pk})


class Upcoming_Products(models.Model):
 name = models.CharField(max_length=300)
 brand = models.CharField(max_length=300)
 release_date = models.DateField(max_length=8)
 description = models.TextField()
 image = models.ImageField(default= 'example.jpg', upload_to='media')
