from django.conf.urls import url
from .views import product_add

app_name = 'producttemp'
urlpatterns = [
    url(r'^$', product_add, name='ProductForm')
]
