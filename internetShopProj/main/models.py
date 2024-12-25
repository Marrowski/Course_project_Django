from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    phone = models.CharField(max_length=12)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)


class Category(models.Model):
    name_category = models.CharField(max_length=25)
    image_category = models.ImageField(upload_to='images/')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    name_product = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2, default=0)
    product_variation = models.CharField(max_length=20, blank=True)

    def sell_price(self):
        return (self.price) - (self.discount_price)


class Attributes(models.Model):
    name_attribute = models.CharField(max_length=35, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50, blank=False)
    text = models.CharField(max_length=255, blank=False)
    is_recommend = models.BooleanField()
    mark = models.IntegerField()


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(blank=True, upload_to='images/')


