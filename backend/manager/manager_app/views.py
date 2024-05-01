from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from manager_app.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

def index(request):
    return render(request, 'manager_app/index.html')

def admins(request):
    # return render(request, 'admins.html')
    data = Admins.objects.all()
    return render(request, 'manager_app/admins.html', {'data': data})

def admins_delete(request, admin_id):
     admin = get_object_or_404(Admins, id_admins=admin_id)

     if request.method == 'POST':
         admin.delete()
         return redirect('admins')
     return redirect('admins')


def admins_toggle_status(request, admin_id):
    admin = get_object_or_404(Admins, id_admins=admin_id)
    if admin.a_status != True:
       admin.a_status = True
    else:
        redirect('admins')
    admin.save()
    return redirect('admins')

def users(request):
    # return render(request, 'users.html')
    data = Users.objects.all()
    return render(request, 'manager_app/users.html', {'data': data})

def users_delete(request, user_id):
     user = get_object_or_404(Users, id_user=user_id)

     if request.method == 'POST':
         user.delete()
         return redirect('users')
     return redirect('users')

def users_toggle_status(request, user_id):
    user = get_object_or_404(Users, id_user=user_id)
    if user.u_status != True:
       user.u_status = True
    else:
        redirect('users')
    user.save()
    return redirect('users')

# def admins_edit(request, admin_id):
#     admin = get_object_or_404(Admins, id_admin=admin_id)
#     if request.method == 'POST':
#         admin.a_username = request.POST.get('a_username')
#         admin.a_name = request.POST.get('


def items(request):
    data = Shoes.objects.all()
    shoes_data = Shoes.objects.all()
    for shoe in shoes_data:
        sizes = shoe.sh_size_array
        for size in sizes:
            size = int(size)
    return render(request, 'manager_app/items.html', {'data': data})

def items_delete(request, item_id):
     item = get_object_or_404(Shoes, id_item=item_id)

     if request.method == 'POST':
         item.delete()
         return redirect('item')
     return redirect('item')

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
    
# def items_form_edit(request, id):
#     item = get_object_or_404(Shoes, id_shoes=id)
#     photos = ShoesImages.objects.filter(item=item)
#     # Either render only the modal content, or a full standalone page
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         template_name = 'manager_app/items.html'
#         if request.method == 'POST':
#             item.sh_name = request.POST.get('sh_name')
#             item.sh_model = request.POST.get('sh_model')
#             item.sh_size_array = request.POST.get('sh_size_array')
#             item.sh_color = request.POST.get('sh_color')
#             item.sh_manufacturer = request.POST.get('sh_manufacturer')
#             item.sh_count = request.POST.get('sh_count')
#             item.sh_price = request.POST.get('sh_price')
#             item.sh_image = request.POST.get('sh_image')
#             item.save()
#             return redirect('items')
#     else:
#         template_name = 'manager_app/items.html'
#     return render(request, template_name, {
#         'item':item,
#         'photos':photos
#     })

def orders(request):
    # return render(request, 'orders.html')
    data = Orders.objects.all()
    for item in data:
        item.order_sum = item.o_count * item.o_shoes.sh_price
    return render(request, 'manager_app/orders.html', {'data': data})

def orders_delete(request, order_id):
     order = get_object_or_404(Orders, id_order=order_id)

     if request.method == 'POST':
         order.delete()
         return redirect('orders')
     return redirect('orders')

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

def reservations_delete(request, reservation_id):
     reservation = get_object_or_404(Reservations, id_reservation=reservation_id)

     if request.method == 'POST':
         reservation.delete()
         return redirect('reservations')
     return redirect('reservations')

def analytics(request):
    return render(request, 'manager_app/analytics.html')

# orders_with_shoes_info = Orders.objects.select_related('o_shoes').all()

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