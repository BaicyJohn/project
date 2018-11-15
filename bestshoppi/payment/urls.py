from django.conf.urls import url
from .views import Payment
from .views import Netbank
from .views import Card
from .views import Cash



app_name = 'payment'
urlpatterns = [

    url(r'^$', Payment, name='Payment'),
    url(r'^$', Card, name='Card'),
    url(r'^$', Netbank, name='Netbank'),
    url(r'^$', Cash, name='Cash'),


]