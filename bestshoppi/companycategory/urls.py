from django.conf.urls import url
from .views import comp_category

app_name = 'companycategory'
urlpatterns = [
    url(r'^$', comp_category, name='CompCatForm')
]