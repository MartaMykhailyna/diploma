from django.urls import path
from . import views


app_name = 'manager_login'

urlpatterns = [
    path('send-email-for-register/', views.register_view, name='send-email-for-register'),
]
