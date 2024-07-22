from django.contrib import admin
from .models import Company, Phone, Laptop, Accessories
from import_export.admin  import ImportExportModelAdmin

admin.site.register(Company)

@admin.register(Phone)
class PhoneAdmin(ImportExportModelAdmin):
    list_display = ["company", "model", "price"]
    list_display_links = ["company", "model", "price"]


@admin.register(Laptop)
class LaptopAdmin(ImportExportModelAdmin):
    list_display = ["company", "model", "price"]
    list_display_links = ["company", "model", "price"]

@admin.register(Accessories)
class AccessoriesAdmin(ImportExportModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name", "price"]
    