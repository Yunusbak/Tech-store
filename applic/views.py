from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Phone, Laptop, Accessories
from .forms import PhoneForm, LaptopForm, AccessoriesForm, RegisterForm
from django.urls import reverse_lazy



def home(request):
        return render(request, "home.html")

def info(request):
    return render(request, "info.html")

    
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            username = form.data.get('username')
            email = form.data.get('email')
            password = form.data.get('password')

            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            return redirect('login')
        return render(request, "register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, "login.html", {"form": form, "message_login": "такого пользователя не существует"})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class PhoneListView(ListView):
    model = Phone
    template_name = "phone.html"
    context_object_name = "phone_obj"

class PhoneDetailView(DetailView):
    model = Phone
    template_name = "phone_detail.html"
    context_object_name = "phone_detail_obj"

class PhoneCreateView(View):
    def get(self, request):
        form = PhoneForm()
        return render(request, "phone_crud.html", {"form": form})

    def post(self, request):
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('phone')
        return render(request, "phone_crud.html", {"form": form})

class PhoneUpdateView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phone, pk=pk)
        form = PhoneForm(instance=phone)
        return render(request, 'phone_update.html', {'form': form})

    def post(self, request, pk):
        phone = get_object_or_404(Phone, pk=pk)
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone')
        return render(request, 'phone_update.html', {'form': form})

class PhoneDeleteView(View):
    def get(self, pk):
        phone = get_object_or_404(Phone, pk=pk)
        phone.delete()
        return redirect('phone')

class LaptopListView(ListView):
    model = Laptop
    template_name = "laptop.html"
    context_object_name = "laptop_obj"

class LaptopDetailView(DetailView):
    model = Laptop
    template_name = "laptop_detail.html"
    context_object_name = "laptop_detail_obj"

class LaptopCreateView(View):
    def get(self, request):
        form = LaptopForm()
        return render(request, "laptop_crud.html", {"form": form})

    def post(self, request):
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('laptop')
        return render(request, "laptop_crud.html", {"form": form})

class LaptopUpdateView(View):
    def get(self, request, pk):
        laptop = get_object_or_404(Laptop, pk=pk)
        form = LaptopForm(instance=laptop)
        return render(request, 'laptop_update.html', {'form': form})

    def post(self, request, pk):
        laptop = get_object_or_404(Laptop, pk=pk)
        form = LaptopForm(request.POST, request.FILES, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('laptop')
        return render(request, 'laptop_update.html', {'form': form})

class LaptopDeleteView(View):
    def get(self, pk):
        laptop = get_object_or_404(Laptop, pk=pk)
        laptop.delete()
        return redirect('laptop')


class AccessoriesListView(ListView):
    model = Accessories
    template_name = "accessories.html"
    context_object_name = "accessories_obj"

class AccessoriesDetailView(DetailView):
    model = Accessories
    template_name = "accessories_detail.html"
    context_object_name = "accessories_detail_obj"

class AccessoriesCreateView(View):
    def get(self, request):
        form = AccessoriesForm()
        return render(request, "accessories_crud.html", {"form": form})

    def post(self, request):
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accessories')
        return render(request, "accessories_crud.html", {"form": form})

class AccessoriesUpdateView(View):
    def get(self, request, pk):
        accessories = get_object_or_404(Accessories, pk=pk)
        form = AccessoriesForm(instance=accessories)
        return render(request, 'accessories_update.html', {'form': form})

    def post(self, request, pk):
        accessories = get_object_or_404(Accessories, pk=pk)
        form = AccessoriesForm(request.POST, request.FILES, instance=accessories)
        if form.is_valid():
            form.save()
            return redirect('accessories')
        return render(request, 'accessories_update.html', {'form': form})

class AccessoriesDeleteView(View):
    def get(self, pk):
        accessories = get_object_or_404(Accessories, pk=pk)
        accessories.delete()
        return redirect('accessories')


def search(request):
    query = request.GET.get('q')
    if query:
        phones = Phone.objects.filter(model__icontains=query)
        laptops = Laptop.objects.filter(model__icontains=query)
        accessories = Accessories.objects.filter(name__icontains=query)
    else:
        phones = Phone.objects.none()
        laptops = Laptop.objects.none()
        accessories = Accessories.objects.none()

    context = {
        'phones': phones,
        'laptops': laptops,
        'accessories': accessories,
    }
    return render(request, 'search.html', context)

def account(request):
    return render(request, "account.html")