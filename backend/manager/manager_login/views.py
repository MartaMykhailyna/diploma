from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subject = 'Умови співпраці та реєстрація'
            message = 'Дякуємо за ваш інтерес! Ми надішлемо вам умови співпраці та посилання на реєстрацію протягом дня.'
            from_email = 'martamykhailyna608@gmail.com'  
            recipient_list = [email]
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Лист було надіслано успішно.')
            except Exception as e:
                messages.error(request, 'Не вдалося надіслати лист. Будь ласка, спробуйте пізніше.')
        else:
            messages.error(request, 'Будь ласка, введіть коректну електронну пошту.')
        return redirect('manager_login:send-email-for-register')
    else:
        return render(request, 'registration/register.html')