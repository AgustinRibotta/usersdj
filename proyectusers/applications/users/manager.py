# Django
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username,  email, password=None, **extra_fields):
        return self._create_user (username, email, password, False, False, False, **extra_fields)

    
    def create_superuser(self, username, email, password=None, **extra_fields):
        # Con el _ la hacemos privada esto evita que se pueda acceder de otro la do que no sea la terminal.
        return self._create_user(username, email, password,True, True, True, **extra_fields)


    # Validacion de codigo
    def cod_validate(self, id_user, cod_register):
        if self.filter(id=id_user, cod_register = cod_register).exists():
            return True
        else:
            return False