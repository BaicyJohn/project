from django.conf.urls import url
from .views import AddtoCart
from .views import delete_item

app_name = 'cart'
urlpatterns = [

    url(r'^$', AddtoCart,name='AddtoCart'),
    url(r'^delete_item/(?P<pk>\d+)/$', delete_item, name='delete_item'),


]
