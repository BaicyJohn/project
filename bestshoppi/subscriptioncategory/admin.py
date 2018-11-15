from django.contrib import admin
from .models import SubscriptionCategory


class SubscriptionCatAdmin(admin.ModelAdmin):
    list_display = ["subcategory_name", "subcategory_description", "subcategory_rate"]


admin.site.register(SubscriptionCategory, SubscriptionCatAdmin)


