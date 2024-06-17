from django.db import models
from enum import Enum
from datetime import datetime, timedelta
from django.db.models import Sum
from django.utils import timezone
import calendar
from manager_login.models import User
# from django.contrib.postgres.fields import ArrayField

class Order_status(Enum):
    accepted = 'accepted'
    paid = 'paid'
    in_processing = 'in processing'
    shipped = 'shipped'
    delivered = 'delivered'
    paid_to_dropper = 'paid to dropper'  
    
class User_role(Enum):
    administartor = 'administartor'
    user = 'user'
       
# class ShoeSize(models.Model):
#     size = models.IntegerField()  
     
class Shoes(models.Model):
    id_shoes = models.AutoField(primary_key=True, unique=True)
    sh_name = models.CharField(max_length=255)
    sh_model = models.CharField(max_length=255)
    sh_size = models.IntegerField(null=False, default=38)
    sh_color = models.CharField(max_length=255)
    sh_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    sh_count = models.IntegerField(null=False, default=1)
    sh_price = models.DecimalField(max_digits=10, decimal_places=2)
    sh_image = models.ImageField(blank=False, upload_to='images/')  # Якщо використано bytea, можна використати BinaryField
    
    class Meta:
        db_table = 'shoes'

# class ShoesImages(models.Model):
#     item = models.ForeignKey(Shoes, related_name='images', on_delete=models.CASCADE)
#     images = models.FileField(upload_to='images/')
#     # is_first = models.BooleanField(default=False)
#     # is_second = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.item.sh_name
    
# class Users(models.Model):
#     id_user = models.IntegerField(primary_key=True)
#     u_username = models.CharField(max_length=255)
#     u_name = models.CharField(max_length=255)
#     u_surname = models.CharField(max_length=255)
#     u_email = models.CharField(max_length=255, blank=True, null=True)
#     u_phone = models.CharField(max_length=13)
#     u_status = models.BooleanField(default=False)
#     u_role = models.CharField(max_length=45,default=User_role.user.name, choices=[(user_role.value, user_role.name) for user_role in User_role])
    
#     class Meta:
#         db_table = 'users'


    
class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    o_shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, db_column='o_shoes')
    o_count = models.IntegerField(null=False, default=1)
    o_sum = models.DecimalField(max_digits=10, decimal_places=2)
    o_recipient = models.CharField(max_length=45, null=False, default='Name,Surname')
    o_address = models.CharField(max_length=100, null=False, default='Address')
    o_comment=models.CharField(max_length=100, null=True)
    o_status = models.CharField(max_length=45, default=Order_status.accepted.value, choices=[(status.value, status.name) for status in Order_status])    
    o_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, db_column='o_user')
    o_date_created = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'orders'

    @classmethod
    def calculate_total_sum(cls):
        return cls.objects.aggregate(total_sum=models.Sum('o_sum'))['total_sum'] or 0

    @classmethod
    def calculate_average_sum(cls):
        total_sum = cls.calculate_total_sum()
        total_orders = cls.objects.count()
        return total_sum / total_orders if total_orders != 0 else 0

    @classmethod
    def find_max_sum(cls):
        return cls.objects.aggregate(max_sum=models.Max('o_sum'))['max_sum'] or 0

    @classmethod
    def find_min_sum(cls):
        return cls.objects.aggregate(min_sum=models.Min('o_sum'))['min_sum'] or 0

    @classmethod
    def calculate_total_sum_for_current_month(cls):
        # Get the current year and month
        current_year = timezone.now().year
        current_month = timezone.now().month

        # Filter orders for the current month
        orders_for_current_month = cls.objects.filter(
            o_date_created__year=current_year,
            o_date_created__month=current_month
        )

        # Calculate the total sum for the current month
        total_sum_for_current_month = orders_for_current_month.aggregate(total_sum=Sum('o_sum'))['total_sum']

        return total_sum_for_current_month or 0  # Return 0 if no orders found for the current month       

    @classmethod
    def calculate_total_sum_for_previous_month(cls):
        # Get the previous month and year
        first_day_of_current_month = timezone.now().replace(day=1)
        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
        previous_month = last_day_of_previous_month.month
        previous_year = last_day_of_previous_month.year

        # Filter orders for the previous month
        orders_for_previous_month = cls.objects.filter(
            o_date_created__year=previous_year,
            o_date_created__month=previous_month
        )

        # Calculate the total sum for the previous month
        total_sum_for_previous_month = orders_for_previous_month.aggregate(total_sum=Sum('o_sum'))['total_sum']

        return total_sum_for_previous_month or 0  # Return 0 if no orders found for the previous month

    @classmethod
    def calculate_percentage_drop(cls):
        current_month_sum = cls.calculate_total_sum_for_current_month()
        previous_month_sum = cls.calculate_total_sum_for_previous_month()

        if previous_month_sum == 0:
            return 0  # Якщо минулого місяця не було продажів, повертаємо 0

        drop_percentage = ((previous_month_sum - current_month_sum) / previous_month_sum) * 100
        return drop_percentage
    
    @classmethod
    def get_sales_data(cls):
        sales_data = cls.objects.filter(
            o_date_created__year=timezone.now().year
        ).values('o_date_created__month').annotate(total_sales=Sum('o_sum')).order_by('o_date_created__month')

        # Перетворення даних у формат для графіка
        sales_by_month = {month: 0 for month in range(1, 13)}
        for data in sales_data:
            sales_by_month[data['o_date_created__month']] = data['total_sales']
        
        return sales_by_month
    
class Reservations(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    r_shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, db_column='r_shoes')
    r_count = models.IntegerField(null=False, default=1)
    r_start_date = models.DateTimeField(default=timezone.now)
    r_end_date = models.DateTimeField(default=timezone.now() + timedelta(hours=3))
    r_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='r_user')

    class Meta:
        db_table = 'reservations'
        
        