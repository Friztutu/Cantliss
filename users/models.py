# base models
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to=r'user_img', default=r'user_img/default.jpg')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
