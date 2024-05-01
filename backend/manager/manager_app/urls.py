from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/', views.admins, name='admins'),
    path('admins-delete/<int:admin_id>/', views.admins_delete, name='admins-delete'),
    path('admins_toggle_status/<int:admin_id>/', views.admins_toggle_status, name='admins_toggle_status'),
    path('items/', views.items, name='items'),
    path('det/<int:id>/', views.items_detailed_view, name='items-photos'),
    path('items-delete/<int:item_id>/', views.items_delete, name='items-delete'),
    # path('edit/<int:id>/', views.items_form_edit, name='items-form-edit'),
    path('users/', views.users, name='users'),
    path('users-delete/<int:user_id>/', views.users_delete, name='users-delete'),
    path('users-toggle-status/<int:user_id>/', views.users_toggle_status, name='users_toggle_status'),
    path('orders/', views.orders, name='orders'),
    path('orders-delete/<int:order_id>/', views.orders_delete, name='orders-delete'),
    path('orders-detail/<int:id>/', views.orders_detailed_view, name='orders-detail'),
    # path("order-sum/", views.order_sum_view, name="order-sum"),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations-delete/<int:reservation_id>/', views.reservations_delete, name='reservations-delete'),
    path('analytics/', views.analytics, name='analytics'),
    # path('convert/<str:currency>/', views.convert_currency, name='convert_currency'),
]
 