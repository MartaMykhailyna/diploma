from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/', views.admins, name='admins'),
    path('items/', views.items, name='items'),
    path('orders/', views.orders, name='orders'),
    path('users/', views.users, name='users'),
    path('analytics/', views.analytics, name='analytics'),
]
