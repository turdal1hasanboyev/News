from django.shortcuts import render, redirect

import re

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomUser


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    return len(password) >= 8

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        image = request.FILES.get('image')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')
        if not validate_email(email):
            messages.error(request, 'Email format is incorrect!')
            return redirect('register')
        if not validate_password(password):
            messages.error(request, 'Password must be at least 8 characters long!')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            image=image,
        )
        user.save()
        messages.success(request, 'You have successfully registered!')
        return redirect('login')
    
        # login sahifaga yo'naltirish

        '''
        user.save()
        messages.success(request, 'You have successfully registered!')
        login(request, user)
        return redirect('home')
        '''

        # to'g'ridan togri login qiladi

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error! The password or username was entered incorrectly')
            return redirect('login')
        
    return render(request, 'login.html')

@login_required        
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')
