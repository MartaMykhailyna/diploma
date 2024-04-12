from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manager_app.urls')),
    path('', include('manager_edit.urls')),
    path('currency/', include('currency_exchange.urls')),
]
