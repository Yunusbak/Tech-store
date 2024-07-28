from django import forms
from django.contrib.auth.models import User
from .models import Phone, Laptop, Accessories

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['company', 'model', 'image', 'price']

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['company', 'model', 'image', 'price']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'image', 'price']


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)
