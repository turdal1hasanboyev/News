from django.contrib.auth.models import UserManager

import re


class CustomUserManager(UserManager):
    def create_user(self, email, first_name, last_name, image=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Users must have a valid email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, image=image, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, image=None, password=None, **extra_fields):
        extra_fields.update({'is_staff': True, 'is_superuser': True})

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not email:
            raise ValueError('Superuser must have an email address')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Superuser must have a valid email address')
        if not first_name:
            raise ValueError('Superuser must have a first name')
        if not last_name:
            raise ValueError('Superuser must have a last name')
        
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, image=image, password=password, **extra_fields)
        user.save(using=self._db)
        return user
