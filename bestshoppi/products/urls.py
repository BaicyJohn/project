from django.conf.urls import url
from .views import product_add,edit_product, delete_product

app_name = 'products'
urlpatterns = [
    url(r'^$', product_add, name='ProductForm'),
    url(r'^edit-product/(?P<pk>\d+)/$', edit_product, name='edit_product'),
    url(r'^delete-product/(?P<pk>\d+)/$', delete_product, name='delete_product'),
]
