from django.shortcuts import render, redirect
from . import forms
from companyregisteration.models import CompanyReg


def edit_profile(request):
    template = 'companyprofile/profile.html'

    post = CompanyReg.objects.get(id=request.session['logid'])

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('companyprofile:edit_profile')

    else:
        form = forms.ProfileForm(instance=post)
        context = {
            'form': form,
            'post': post,

        }

    return render(request, template, context)
