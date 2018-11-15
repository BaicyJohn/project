from django.shortcuts import render,redirect
from .import forms
from custregisteration.models import CustomerReg
from django.contrib import messages


def custreghome(request):
    return render(request, 'customerhome/custhome.html', {'logidd': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =userObj['password']
            if CustomerReg.objects.filter(username=username).exists() and CustomerReg.objects.filter(password=password).exists():
                obj = CustomerReg.objects.get(username=username)
                request.session['logid'] = obj.id
                return redirect('customerlogin:custreghome')
            else:
                messages.info(request, 'incorrect username or password')
                return render(request, 'customer_login/login.html', {'form': form})
    else:
        form = forms.LoginForms()
    return render(request, 'customer_login/login.html', {'form': form})
