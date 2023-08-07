# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .manager import UserManager

# User Model de esta manera definimos totalmente el registro de usaurio
class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES =(
        ('M' , 'Male'),
        ('F' , 'Famele'),
        ('O' , 'Other'),
    )
    
    username = models.CharField(
        max_length=10,
        unique=True,
    )
    email = models.EmailField()
    name = models.CharField(
        max_length=30,
        blank= True,
    )
    last_name = models.CharField(
        max_length=30,
        blank= True,
    )
    gender = models.CharField(
        max_length=1,
        choices= GENDER_CHOICES,
        blank=True
    )
    
    USERNAME_FIELD ='username'
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.name + ' ' + self.last_name