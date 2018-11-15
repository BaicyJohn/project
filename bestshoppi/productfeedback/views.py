from django.shortcuts import render, redirect
from . import forms
from .models import CompFeedback


def comp_feedback(request):
    login_id = request.session['logid']
    model_object = CompFeedback.objects.filter(comp_id=login_id)
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            FeedbackObj = form.cleaned_data
            content = FeedbackObj['content']
            date = FeedbackObj['date']

            a = CompFeedback(content=content, date=date, comp_id=login_id)

            a.save()

            return redirect('productfeedback:FeedbackForm')
    else:
        form = forms.FeedbackForm
    return render(request, "compfeedback/feedback.html", {'form': form, 'data': model_object, 'IDD': login_id})

