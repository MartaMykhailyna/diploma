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


def users(request):
    # return render(request, 'users.html')
    data = Users.objects.all()
    return render(request, 'users.html', {'data': data})


def analytics(request):
    return render(request, 'analytics.html')