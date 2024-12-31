from django.db import models

from django.contrib.auth.models import AbstractUser

from ..common.models import BaseModel
from .managers import CustomUserManager


class CustomUser(AbstractUser, BaseModel):
    """Custom User Model"""
    username = None
    email = models.EmailField(max_length=150, unique=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.email
