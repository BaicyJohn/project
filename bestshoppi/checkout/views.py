from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from purchase.models import Purchase
from custregisteration.models import CustomerReg
from .import forms


def Checkout(request):

    p = CustomerReg.objects.get(id=request.session['logid'])
    #model_object = Purchase.objects.filter(Custid=p.id)
    #model_object=p.id
    model_object = Purchase.objects.filter(Custid=p.id, status=0).last()
    #c = model_object.objects.last()
    qt = Purchase.objects.filter(Custid=p.id).aggregate(Grand_Total=Sum('total'))
    #ct = Purchase.objects.filter(Custid=p.id).aggregate(No_of_items=Count('ProductName'))
    item = Purchase.objects.filter(Custid=p.id).aggregate(item=Sum('no_item'))
    form = forms.CheckoutForm



    return render(request, "checkout/checkout.html", {'form':form, 'data': p, 'd': qt, 'item':item,'order':model_object})
