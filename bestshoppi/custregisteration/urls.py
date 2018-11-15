from django.conf.urls import url
from .views import custreg

app_name = 'custregisteration'
urlpatterns = [
    url(r'^$', custreg, name='CustRegForm')
]