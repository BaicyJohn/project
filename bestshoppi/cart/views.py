from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from purchase.models import Purchase
from custregisteration.models import CustomerReg

def AddtoCart(request):
    p = CustomerReg.objects.get(id=request.session['logid'])
    model_object = Purchase.objects.filter(Custid=p.id)
    qt = Purchase.objects.filter(Custid=p.id).aggregate(Grand_Total=Sum('total'))
    item = Purchase.objects.filter(Custid=p.id).aggregate(item=Sum('no_item'))


    return render(request, "AddtoCart/Cart.html", {'data': model_object, 'd': qt, 'item':item})
def delete_item(request,pk):
    post = get_object_or_404(Purchase, pk=pk)
    post.delete()
    return render(request, "AddtoCart/Cart.html")