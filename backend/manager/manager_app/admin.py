from django.contrib import admin
from .models import *

admin.site.register(Shoes)
# admin.site.register(User)
admin.site.register(Orders)
admin.site.register(Reservations)

