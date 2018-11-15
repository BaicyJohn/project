from django.shortcuts import render, get_object_or_404
from products.models import Product
from quantity.models import Quantity
from custregisteration.models import CustomerReg
from django.contrib import messages
from . import forms
from .models import Purchase


def purchase_item(request, pk):
    model_object = Product.objects.get(id=pk)
    model_obj = Quantity.objects.get(Productid=pk)
    p= CustomerReg.objects.get(id=request.session['logid'])
    # pro = Product.objects.get(id=pk)
    # return render(request, "purchase/purchase.html", {'data': model_object, 'd': model_obj})

    if request.method == 'POST':
        form = forms.PurchaseForm(request.POST)
        if form.is_valid():

            # form = forms.PurchaseForm(request.POST)
            pro = Product.objects.get(id=pk)
            dd = Quantity.objects.get(Productid=pk)

            ProductObj = form.cleaned_data
            quantity = ProductObj['no_item']
            rate = pro.product_rate

            r = dd.quantity

            if int(r) < int(quantity):
                messages.info(request, 'Stock out')
            else:
                total = int(rate) * int(quantity)
                balq = int(r)-int(quantity)
                dd.quantity = balq
                # b = post(quantity=model_obj.quantity, Productid=pk)
                dd.save()
                a = Purchase(Custid=p.id, Productid=pk, ProductName=model_object.product_name, no_item=quantity, total=total)
                a.save()
                messages.info(request, 'Added to Cart')
                return render(request, "productlist/productlist.html")

    else:
        form = forms.PurchaseForm
        # form1= ProductForm

    return render(request, "purchase/purchase.html", {'form': form, 'data': model_object, 'd': model_obj})
