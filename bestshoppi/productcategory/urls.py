from django.conf.urls import url
from .views import product_category

app_name = 'productcategory'
urlpatterns = [
    url(r'^$', product_category, name='ProductCatForm')
]