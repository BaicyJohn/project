from django.conf.urls import url
from .views import purchase_item


app_name = 'purchase'
urlpatterns = [
    url(r'^purchase/(?P<pk>\d+)/$', purchase_item, name='purchase'),

]