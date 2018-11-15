from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_rate", "product_description", "product_image", "comp_id"]


admin.site.register(Product, ProductAdmin)

