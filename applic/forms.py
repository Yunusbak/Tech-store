from django.forms import ModelForm
from .models import Phone, Accessories, Laptop

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ["company", "model", "image", "price"]

class AccessoriesForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ["name", "image", "price"]


class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ["company", "model", "image", "price"]


from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)
