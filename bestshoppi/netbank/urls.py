from django.conf.urls import url


from .views import netbank




app_name = 'netbank'
urlpatterns = [


    url(r'^$', netbank, name='netbank'),




]