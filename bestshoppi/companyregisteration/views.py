from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from . import forms


def Compreg(request):

    if request.method == 'POST':

        form = forms.CompRegForm(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['email_id']
            username = obj['username']
            password = obj['password']
            instance.save()
            email = EmailMessage('Bestshoppe Company Registeration', 'You are succesfully registered! username:   ' + username + '      password:   ' + password + '', to=[mail])
            email.send()


            return redirect('companyregisteration:CompRegForm')
    else:
        form = forms.CompRegForm

    return render(request, "companyreg/comp_reg.html", {'form': form})
