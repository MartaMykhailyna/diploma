from django.urls import path
from manager_login.views import *

app_name='manager_login'

urlpatterns = [
    path('login/', login, name='login'),
    # path('', users_login, name='users_login'),
]