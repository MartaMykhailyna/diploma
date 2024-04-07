from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from manager_app.models import *

def index(request):
    return render(request, 'index.html')

def admins(request):
    # return render(request, 'admins.html')
    data = Admins.objects.all()
    return render(request, 'admins.html', {'data': data})

def items(request):
    # return render(request, 'items.html')
    data = Shoes.objects.all()
    return render(request, 'items.html', {'data': data})

def orders(request):
    # return render(request, 'orders.html')
    data = Orders.objects.all()
    return render(request, 'orders.html', {'data': data})

def reservations(request):
    # return render(request, 'orders.html')
    data = Reservations.objects.all()
    return render(request, 'reservations.html', {'data': data})


def users(request):
    # return render(request, 'users.html')
    data = Users.objects.all()
    return render(request, 'users.html', {'data': data})


def analytics(request):
    return render(request, 'analytics.html')

# Отримуємо всі замовлення з додатковою інформацією про взуття
# orders_with_shoes_info = Orders.objects.select_related('o_shoes').all()

# # Тепер ви можете перебрати ці замовлення та отримати інформацію про взуття
# for order in orders_with_shoes_info:
#     print("Замовлення ID:", order.id_order)
#     print("Колір взуття:", order.o_shoes.sh_color)
#     print("Модель взуття:", order.o_shoes.sh_model)
