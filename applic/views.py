from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Phone, Laptop, Accessories
from django.urls import reverse
from .forms import PhoneForm, AccessoriesForm, LaptopForm



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


def phone_view(request):
    phone_obj = Phone.objects.all()
    context = {"phone_obj" : phone_obj}
    return render(request, "phone.html", context=context)


def phone_detail_view(request, id):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    phone_detail_obj = get_object_or_404(Phone, id=id)
    context = {"phone_detail_obj": phone_detail_obj}
    return render(request, "phone_detail.html", context=context)


def laptop_view(request):
    laptop_obj = Laptop.objects.all()
    context = {"laptop_obj": laptop_obj}
    return render(request, "laptop.html", context=context)

def laptop_detail_view(request, id):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    laptop_detail_obj = get_object_or_404(Laptop, id=id)
    context = {"laptop_detail_obj": laptop_detail_obj}
    return render(request, "laptop_detail.html", context=context)

def accessories_view(request):
    accessories_obj = Accessories.objects.all()
    context = {"accessories_obj" : accessories_obj}
    return render(request, "accessories.html", context=context)


def accessories_detail_view(request, id):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    accessories_detail_obj = get_object_or_404(Accessories, id=id)
    context = {"accessories_detail_obj": accessories_detail_obj}
    return render(request, "accessories_detail.html", context=context)


def account_view(request):
    context = {"user": request.user}
    return render(request, "account.html", context=context)

def phone_create(request):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    elif request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("phone")
        
    form = PhoneForm()
    context = {"form": form}
    return render(request, "phone_crud.html", context=context)

def phone_delete(request, id):
    phone_delete_obj = get_object_or_404(Phone, id = id)
    phone_delete_obj.delete()
    return redirect("phone")

def laptop_create(request):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    if request.method == 'POST':
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("laptop")
    form = LaptopForm()
    context = {"form": form}
    return render(request, "laptop_crud.html", context=context)

def laptop_delete(request, id):
    laptop_delete_obj = get_object_or_404(Laptop, id = id)
    laptop_delete_obj.delete()
    return redirect("laptop")


def accessories_create(request):
    if not request.user.is_authenticated:
        return redirect(reverse("register"))
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accessories")
            
    form = AccessoriesForm()
    context = {"form": form}
    return render(request, "accessories_crud.html", context=context)

def accessories_delete(request, id):
    accessories_delete_obj = get_object_or_404(Accessories, id = id)
    accessories_delete_obj.delete()
    return redirect("accessories")

def phone_update(request, id):
    phone_update_obj = get_object_or_404(Phone, id=id)  
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone_update_obj)
        if form.is_valid():
            form.save()
            return redirect("phone")  
    else:
        form = PhoneForm(instance=phone_update_obj)
    return render(request, 'phone_update.html', {'form': form})

def laptop_update(request, id):
    laptop_update_obj = get_object_or_404(Laptop, id=id)
    if request.method == 'POST':
        form = LaptopForm(request.POST, request.FILES, instance=laptop_update_obj)
        if form.is_valid():
            form.save()
            return redirect("laptop")
        
    else:
        form=LaptopForm(instance=laptop_update_obj)
    return render(request, "laptop_update.html", {"form" : form})
    


def accessories_update(request, id):
    accessories_update_obj = get_object_or_404(Accessories, id=id)
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES, instance=accessories_update_obj)
        if form.is_valid():
            form.save()
            return redirect("accessories")
        
    else:
        form=AccessoriesForm(instance=accessories_update_obj)
    return render(request, "accessories_update.html", {"form" : form})


def info(request):
    return render(request, "info.html")