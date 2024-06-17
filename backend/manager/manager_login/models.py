from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

class User_role(Enum):
    administartor = 'administartor'
    user = 'user'

class User(AbstractUser):
    id_user = models.IntegerField(primary_key=True)
    u_username = models.CharField(max_length=255)
    u_name = models.CharField(max_length=255)
    u_surname = models.CharField(max_length=255)
    u_email = models.CharField(max_length=255, blank=True, null=True)
    u_phone = models.CharField(max_length=13)
    u_status = models.BooleanField(default=False)
    u_role = models.CharField(max_length=45,default=User_role.user.name, choices=[(user_role.value, user_role.name) for user_role in User_role])
    
    class Meta:
        db_table = 'users'