from django.contrib import admin
from .models import ProductCategory


class ProductCatAdmin(admin.ModelAdmin):
    list_display = ["pcategory_name"]


admin.site.register(ProductCategory, ProductCatAdmin)
