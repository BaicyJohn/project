from django.conf.urls import url
from .views import compreg_home, login

app_name = 'companylogin'
urlpatterns = [
    url(r'^$', login, name='LoginForms'),
    url(r'^comphome',  compreg_home, name='compreg_home')
]