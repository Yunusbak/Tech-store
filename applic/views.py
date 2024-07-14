from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Phone, Laptop, Accessories, Pokupka
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([first_name, last_name, username, email, password, password2]):
            return render(request, "register.html", context={"message": "Пожалуйста, заполните все поля"})

        if password != password2:
            return render(request, "register.html", context={"message_password": "Пароли не совпадают"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", context={"message_user": "Пользователь с таким именем уже существует"})

        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", context={"message_login": "такого пользователя не существует"})
    
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def phone(request):
    phone_obj = Phone.objects.all()
    context = {"phone_obj" : phone_obj}
    return render(request, "phone.html", context=context)

@login_required
def laptop(request):
    laptop_obj = Laptop.objects.all()
    context = {"laptop_obj": laptop_obj}
    return render(request, "laptop.html", context=context)

@login_required
def accessories(request):
    accessories_obj = Accessories.objects.all()
    context = {"accessories_obj" : accessories_obj}
    return render(request, "accessories.html", context=context)


def account_view(request):
    context = {"user": request.user}
    return render(request, "account.html", context=context)


def pokupka_view(request):
    pokupki = Pokupka.objects.all()
    return render(request, 'pokupka.html', {'pokupki': pokupki})
