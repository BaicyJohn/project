from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(District, DistrictAdmin)


