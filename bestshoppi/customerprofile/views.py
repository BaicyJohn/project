from django.shortcuts import render, redirect
from . import forms
from custregisteration.models import CustomerReg


def edit_profile(request):
    template = 'custprofile/profile.html'

    post = CustomerReg.objects.get(id=request.session['logid'])

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('customerprofile:edit_profile')

    else:
        form = forms.ProfileForm(instance=post)
        context = {
            'form': form,
            'post': post,

        }

    return render(request, template, context)
