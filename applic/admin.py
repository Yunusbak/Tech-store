from django.contrib import admin
from .models import Company, Phone, Laptop, Accessories

admin.site.register(Company)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ["company", "model", "price"]
    list_display_links = ["company", "model", "price"]

admin.site.register(Phone, PhoneAdmin)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ["company", "model", "price"]
    list_display_links = ["company", "model", "price"]

admin.site.register(Laptop, LaptopAdmin)

class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name", "price"]

admin.site.register(Accessories, AccessoriesAdmin)
