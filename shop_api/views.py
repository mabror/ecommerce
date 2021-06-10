from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import RegisterForms, LoginForms
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "main/index.html", {})


def register(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')

    form = RegisterForms()
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


def login_check(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main-page')

    form = LoginForms()
    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)
