from django.shortcuts import render, redirect

from random import randint
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def random_code_view(request):
    if request.user.is_authenticated:
        logout(request)
        context = {
            'random_code': randint(1000, 9999)
        }
        return render(request, 'random_code/main.html', context)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form = LoginForm()
                return render(request, 'random_code/main.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'random_code/main.html', {'form': form})
