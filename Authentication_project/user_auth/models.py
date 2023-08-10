from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import UserManager
# from ...ProductManagementService.ProductManagement.models import Product


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # fav_products = models.ManyToManyField('FavProducts',blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
# class FavoriteProductSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
#     product_id = serializers.IntegerField()