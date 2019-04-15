from django.shortcuts import render, redirect
from forms.contact_forms import ContactForm
from forms.auth_forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def home_page(request):
    pass


def about_page(request):
    pass


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to Contact Page',
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('/login')
        else:
            print("Error")
        context['form'] = LoginForm()
    return render(request, 'auth/login.html', context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create(username=username, email=email, password=password)
        return redirect('/')
    return render(request, 'auth/register.html', context)
