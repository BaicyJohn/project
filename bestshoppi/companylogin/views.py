from django.shortcuts import render,redirect
from .import forms
from companyregisteration.models import CompanyReg


def compreg_home(request):
    return render(request, 'companyhome/comp_home.html', {'logidd': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =userObj['password']
            if CompanyReg.objects.filter(username=username).exists() and CompanyReg.objects.filter(password=password).exists():
                obj = CompanyReg.objects.get(username=username)
                request.session['logid'] = obj.id
                return redirect('companylogin:compreg_home')
            else:
                return render(request, 'company_login/comp_login.html', {'form': form})
    else:
        form = forms.LoginForms()
    return render(request, 'company_login/comp_login.html', {'form': form})
