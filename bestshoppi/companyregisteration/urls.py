from django.conf.urls import url
from .views import Compreg

app_name = 'companyregisteration'
urlpatterns = [
    url(r'^$', Compreg, name='CompRegForm')
]