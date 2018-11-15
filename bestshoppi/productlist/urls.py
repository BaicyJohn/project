from django.conf.urls import url
from .views import listProduct

app_name = 'productlist'
urlpatterns = [

    url(r'^$', listProduct,name='listProduct'),


]
