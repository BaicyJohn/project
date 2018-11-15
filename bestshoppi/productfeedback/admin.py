from django.contrib import admin
from .models import CompFeedback


class CompFeedAdmin(admin.ModelAdmin):
    list_display = ["content", "date", "comp_id"]


admin.site.register(CompFeedback, CompFeedAdmin)
