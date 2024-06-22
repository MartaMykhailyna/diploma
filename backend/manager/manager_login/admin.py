# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     # form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms
from django.conf import settings

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "u_phone", "u_role"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('u_phone', 'u_role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('u_phone', 'u_role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
