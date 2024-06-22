from django.urls import path, include
from . import views

app_name = 'manager_add'

urlpatterns = [
    path('items/add_item/', views.add_item, name='add-item'),
    path('orders/add_order/', views.add_order, name='add-order'),
    path('reservations/add_reservation/', views.add_reservation, name='add-reservation'),
    ]
