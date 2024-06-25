from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import *

def user_login(request):
    return render(request, 'auth/login.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(request, username=user.email, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'User registered and logged in successfully.')
                return redirect('auth:login')
            else:
                error_message = 'User registration failed. '
                for field, errors in form.errors.items():
                    error_message += f"{field}: {', '.join(errors)}. "
                messages.error(request, error_message.strip())
        else:
            error_message = 'User registration failed. '
            for field, errors in form.errors.items():
                error_message += f"{field}: {', '.join(errors)}. "
            messages.error(request, error_message.strip())
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'auth/register.html', context)