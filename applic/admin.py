from django.contrib import admin
from .models import Company, Phone, Laptop, Accessories

admin.site.register(Company)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ["company", "model", "price"]

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ["company", "model", "price"]

@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
