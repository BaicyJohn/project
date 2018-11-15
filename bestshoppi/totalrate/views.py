from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from quantity.models import Quantity
from totalrate.models import TotalRate
#from products.forms import ProductForm

#from .models import Quantity

from .import forms


def add_quantity(request, pk):



    if request.method == 'POST':
        form = forms.TotalRateForm(request.POST)
        pro = Product.objects.get(id=pk)
        dd = Quantity.objects.get(Productid=pk)
        ProductObj = form.cleaned_data
        quantity = ProductObj['quantity']
        rate = pro.product_rate

        r = dd.quantity
        if form.is_valid():
          if r < quantity:
             messages.info(request, 'Stock out')
          else:
            total=rate*quantity
            a = TotalRate(no_item=quantity, total=total, Productid=pk)
            a.save()





            # q = Quantity.objects.get(Productid=pk)
        #if form.is_valid():
           # a =Q(no_item=quantity,total=total, Productid=pk)
          #  a.save()

            # return redirect('quantity:QuantityForm')
            # ProductObj = form.cleaned_data
            # quantity = ProductObj['quantity']
            # if Quantity.objects.filter(Productid=pk).exists():
            # post = get_object_or_404(Quantity, Productid=pk)

        # if form.is_valid():
        # ProductObj = form.cleaned_data
        # quantity = ProductObj['quantity']
        # a = Quantity(quantity=quantity, Productid=pk)
        # a.save()

    else:
        form = forms.TotalRateForm
        #form1= ProductForm

    return render(request, "purchase/purchase.html", {'form': form})
