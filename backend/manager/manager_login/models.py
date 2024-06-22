# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from enum import Enum

# class UserRole(Enum):
#     administrator = 'administrator'
#     user = 'user'

# class CustomUser(AbstractUser):
#     id_user = models.AutoField(primary_key=True)
#     u_phone = models.CharField(max_length=13)
#     u_role = models.CharField(max_length=45, default=UserRole.user.name, choices=[(role.value, role.name) for role in UserRole])
#     groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
#     class Meta:
#         db_table = 'users'
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings
from enum import Enum

class UserRole(Enum):
    administrator = 'administrator'
    user = 'user'

class CustomUser(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    u_phone = models.CharField(max_length=13)
    u_role = models.CharField(max_length=45, default=UserRole.user.value, choices=[(role.value, role.name) for role in UserRole])
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    class Meta:
        db_table = 'users'
