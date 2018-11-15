from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from purchase.models import Purchase
from custregisteration.models import CustomerReg
from django.contrib import messages


def Payment(request):
    p = CustomerReg.objects.get(id=request.session['logid'])
    # model_object = Purchase.objects.filter(Custid=p.id)
    # model_object=p.id
    model_object = Purchase.objects.filter(Custid=p.id, status=0).last()
    # c = model_object.objects.last()
    qt = Purchase.objects.filter(Custid=p.id).aggregate(Grand_Total=Sum('total'))
    # ct = Purchase.objects.filter(Custid=p.id).aggregate(No_of_items=Count('ProductName'))
    item = Purchase.objects.filter(Custid=p.id).aggregate(item=Sum('no_item'))

    return render(request, "payment1/paymentmethod1.html", {'d': qt, 'item': item, 'order': model_object})



def Card(request):
    return render(request, "payment/CardPayment.html")

def Netbank(request):
    return render(request, "payment/CardPayment.html")

def Cash(request):
    return render(request, "payment/FinalPage.html")


    #if request.method == 'POST':

       # a = request.POST.get('method', '')=='on'
       # return render(request, "payment/PaymentMethod.html", {'a': a})
        #return redirect('payment:Card')
   # else:
       # return redirect('payment:Payment')

   # return render(request, "payment/PaymentMethod.html", {'a': a})