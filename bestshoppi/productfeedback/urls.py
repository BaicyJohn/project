from django.conf.urls import url
from .views import comp_feedback

app_name = 'productfeedback'
urlpatterns = [
    url(r'^$', comp_feedback, name='FeedbackForm')
]