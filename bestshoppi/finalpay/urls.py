from django.conf.urls import url


from .views import finalpay




app_name = 'finalpay'
urlpatterns = [


    url(r'^$', finalpay, name='finalpay'),




]