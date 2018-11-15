from django.conf.urls import url
from .views import edit_profile

app_name = 'customerprofile'
urlpatterns = [

    url(r'^edit-profile$', edit_profile, name='edit_profile'),


]
