from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from manager_app.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

def index(request):
    return render(request, 'manager_app/index.html')

def admins(request):
    # return render(request, 'admins.html')
    data = Admins.objects.all()
    return render(request, 'manager_app/admins.html', {'data': data})

def items(request):
    # return render(request, 'items.html')
    # data = Shoes.objects.all()
    # shoes_data = Shoes.objects.all()
    # for shoe in shoes_data:
    #     sizes = shoe.sizes.all()
    #     for size in sizes:
    #         print(size.size)
    # return render(request, 'manager_app/items.html', {'data': data})
    data = Shoes.objects.all()
    shoes_data = Shoes.objects.all()
    for shoe in shoes_data:
        sizes = shoe.sh_size_array
        for size in sizes:
            size = int(size)
    return render(request, 'manager_app/items.html', {'data': data})


def items_detailed_view(request, id):
    item = get_object_or_404(Shoes, id_shoes=id)
    photos = ShoesImages.objects.filter(item=item)
    # Either render only the modal content, or a full standalone page
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template_name = 'manager_app/items.html'
    else:
        template_name = 'manager_app/items.html'
    return render(request, template_name, {
        'item':item,
        'photos':photos
    })

def users(request):
    # return render(request, 'users.html')
    data = Users.objects.all()
    return render(request, 'manager_app/users.html', {'data': data})

def orders(request):
    # return render(request, 'orders.html')
    data = Orders.objects.all()
    for item in data:
        item.order_sum = item.o_count * item.o_shoes.sh_price
    return render(request, 'manager_app/orders.html', {'data': data})

def orders_detailed_view(request, id):
    item = get_object_or_404(Orders, id_order=id)
    # photos = ShoesImages.objects.filter(item=item)
    # Either render only the modal content, or a full standalone page
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template_name = 'manager_app/orders.html'
    else:
        template_name = 'manager_app/orders.html'
    return render(request, template_name, {
        'item':item,
        
    })
    
# def order_sum_view(request):
    # total_sum = Orders.objects.aggregate(total_sum=Sum(F('o_count') * F('o_shoes__sh_price')))
    # order_sum = total_sum['total_sum'] if total_sum['total_sum'] else 0
    # return render(request, 'orders.html', {'order_sum': order_sum})


def reservations(request):
    # return render(request, 'orders.html')
    data = Reservations.objects.all()
    return render(request, 'manager_app/reservations.html', {'data': data})

def analytics(request):
    return render(request, 'manager_app/analytics.html')

# Отримуємо всі замовлення з додатковою інформацією про взуття
# orders_with_shoes_info = Orders.objects.select_related('o_shoes').all()

# # Тепер ви можете перебрати ці замовлення та отримати інформацію про взуття
# for order in orders_with_shoes_info:
#     print("Замовлення ID:", order.id_order)
#     print("Колір взуття:", order.o_shoes.sh_color)
#     print("Модель взуття:", order.o_shoes.sh_model)

@receiver(post_save, sender=Orders)
def update_shoes_count_on_order_create(sender, instance, created, **kwargs):
    if created:
        shoes = instance.o_shoes
        shoes.sh_count -= instance.o_count
        shoes.save()

@receiver(post_save, sender=Reservations)
def update_shoes_count_on_reservation_create(sender, instance, created, **kwargs):
    if created:
        shoes = instance.r_shoes
        shoes.sh_count -= instance.r_count
        shoes.save()