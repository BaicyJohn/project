from django.conf.urls import url


from .views import index




app_name = 'index'
urlpatterns = [


    url(r'^$', index, name='index'),




]