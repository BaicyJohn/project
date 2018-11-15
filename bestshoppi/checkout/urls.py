from django.conf.urls import url
from .views import Checkout


app_name = 'checkout'
urlpatterns = [

    url(r'^$', Checkout,name='Checkout'),
]