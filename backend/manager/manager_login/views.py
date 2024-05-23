from django.shortcuts import render, redirect
from .forms import LoginForm
from manager_app.models import Users
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data['email_or_username']
            password = form.cleaned_data['password']

            # Check if the input is an email or username
            if '@' in email_or_username:
                user = Users.objects.filter(u_email=email_or_username, u_phone=password).first()
            else:
                user = Users.objects.filter(u_username=email_or_username, u_phone=password).first()

            if user:
                # Perform login operation
                auth_login(request, user)
                
                # Check the user's role and redirect accordingly
                if user.u_role == 'admin':
                    return redirect('manager_app:index_for_admin')  # Замініть на фактичний шлях до сторінки адміністратора
                elif user.u_role == 'user':
                    return redirect('manager_app:index_for_user')  # Замініть на фактичний шлях до сторінки користувача
                else:
                    messages.error(request, 'У вас немає доступу до цієї системи.')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    
    return render(request, 'manager_login/login.html', {'form': form})

# def users_login(request):
#     form = LoginForm(request.POST)
#     if form.is_valid():
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['password']

#             user = Users.objects.filter(u_email=email, u_phone=phone).first()
#             if user:
#                 return redirect('index')
#             else:
#                 messages.error(request, 'Invalid login credentials.')
#     else:
#         form = LoginForm()

    # return render(request, 'manager_login/login.html', {'form': form})
