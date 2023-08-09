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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    cod_register = models.CharField(
        'Registration code', 
        max_length=6,
        blank=True,
    )
    
    # Le indicamos en base a que va a crear el usuario
    USERNAME_FIELD ='username'
    
    # Le indicamos cuales van a ser los requisitos
    REQUIRED_FIELDS =['email',]
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.name + ' ' + self.last_name