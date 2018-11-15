from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from quantity.models import Quantity
#from products.forms import ProductForm

from .models import Quantity
from .import forms


def add_quantity(request, pk):
    pro = Product.objects.get(id=pk)
    idd =pro.id
    messages.info(request, idd)

    if request.method == 'POST':

        if Quantity.objects.filter(Productid=pk).exists():
            post = get_object_or_404(Quantity, Productid=pk)

            form = forms.QuantityForm(request.POST, instance=post)

            # q = Quantity.objects.get(Productid=pk)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

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

            form = forms.QuantityForm(request.POST)
            if form.is_valid():
                ProductObj = form.cleaned_data
                quantity = ProductObj['quantity']

            # pro_obj= Product.objects.get(id=pk)

                a = Quantity(quantity=quantity, Productid=pk)
                a.save()
        # pro_obj = Product.objects.last()
        # idd = pro_obj.id
        # messages.info(request, idd)
        # b = Stock(stock_name=idd, quantity=0)
        # b.save()

        # return redirect("quantity:QuantityForm")
    else:
        form = forms.QuantityForm
        #form1= ProductForm

    return render(request, "quantity/quantity.html", {'form': form, 'data': pro})
