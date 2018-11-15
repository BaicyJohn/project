from django.conf.urls import  url
from .views import custreghome, login

app_name = 'customerlogin'
urlpatterns = [
    url(r'^$', login, name='LoginForms'),
    url(r'^custhome',  custreghome, name='custreghome')
]