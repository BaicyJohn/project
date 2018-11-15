from django import forms
from . import models


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.CompFeedback
        fields = ['content', 'date']
