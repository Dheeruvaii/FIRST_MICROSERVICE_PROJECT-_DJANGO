from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField(max_length=100)
    productPrice = models.IntegerField()
    productQuantity = models.IntegerField()
    productCategory = models.CharField(max_length=100, default='')

class FavProducts(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField( blank=True, null=True)
