from django.conf.urls import url


from .views import Card




app_name = 'card'
urlpatterns = [


    url(r'^$', Card, name='Card'),




]