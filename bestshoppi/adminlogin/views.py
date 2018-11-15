from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate
from django.apps import apps
#from Centers.models import Centers
from django.contrib.auth.models import User


def adminhome(request):
    return render(request,'Admin/AdminHome.html',{'logid':request.session['logid']})





def login(request):
    if request.method == 'POST':
        form = forms.Login_Forms(request.POST, request.FILES)
        if form.is_valid():
            userobj = form.cleaned_data
            username = userobj['username']
            password = userobj['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['logid'] = user.id
                request.session['logname'] = user.username
                return redirect('Login:adminhome')
            else:
                 return render(request, 'adminlogin\Login.html', {'form': form})


        else:
            form = forms.Login_Forms()
            return render(request, 'adminlogin\Login.html', {'form': form})
    else:
        form = forms.Login_Forms()
        return render(request, 'adminlogin\Login.html', {'form': form})





