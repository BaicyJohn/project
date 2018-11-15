from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
#from django.core.exceptions import ValidationError
from .import models
from .import forms



#def clean_email(self):
   # email = self.cleaned_data['email']
   # if models.CustomerReg.objects.filter(email=email).exists():
       # raise forms.ValidationError("Email already exists")
    #return email





def custreg(request):
    if request.method == 'POST':
        form = forms.CustRegForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['email']
            username = obj['username']
            password = obj['password']
            confirm = obj['confirm']
            minlen = 8
            username_qs = models.CustomerReg.objects.filter(username=username)
            if username_qs.exists():
                messages.info(request, 'username already exists!')

            elif len(password) < minlen:
                messages.info(request, 'password should be alleast 8 characters!')
            elif password == confirm:
                messages.info(request, 'You inserted successfully!')
                instance.save()

           # if password == confirm:
              #  if len(password) < minlen:
                   # messages.info(request, 'password should be alleast 8 characters!')
                #messages.info(request, 'You inserted successfully!')
                #instance.save()


                email = EmailMessage('Bestshoppe Customer Registeration',
                                 'You are succesfully registered! username:   ' + username + '      password:   ' + password + '',
                                 to=[mail])
                email.send()

                #return redirect('custregisteration:CustRegForm')
            else:
                messages.info(request, 'password and confirm password not matching!')

                form = forms.CustRegForm

            return render(request, "customer_reg/customer_reg.html", {'form': form})
    else:
        form = forms.CustRegForm
        msg = "Not inserted"
    return render(request, "customer_reg/customer_reg.html", {'form': form, 'msg': msg})