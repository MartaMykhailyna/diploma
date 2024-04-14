from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/', views.admins, name='admins'),
    path('items/', views.items, name='items'),
    path('det/<int:id>/', views.items_detailed_view, name='items-photos'),
    path('users/', views.users, name='users'),
    path('orders/', views.orders, name='orders'),
    path('orders-detail/<int:id>/', views.orders_detailed_view, name='orders-detail'),
    # path("order-sum/", views.order_sum_view, name="order-sum"),
    path('reservations/', views.reservations, name='reservations'),
    path('analytics/', views.analytics, name='analytics'),
    # path('convert/<str:currency>/', views.convert_currency, name='convert_currency'),
]
