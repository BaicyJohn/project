from django.contrib import admin
from .models import CompanyCategory


class CompanyCatAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_description"]


admin.site.register(CompanyCategory, CompanyCatAdmin)

