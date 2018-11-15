from django.conf.urls import url
from .views import add_quantity

app_name = 'quantity'
urlpatterns = [
    url(r'^add_quantity/(?P<pk>\d+)/$', add_quantity, name='QuantityForm'),
]