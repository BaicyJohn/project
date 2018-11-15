from django.contrib import admin
from .models import CustomerReg



class CustRegAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "dob", "email", "contactno", "username", "password"]


admin.site.register(CustomerReg, CustRegAdmin)


