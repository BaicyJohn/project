from django.shortcuts import render, redirect
from . import forms
from .models import Product


def product_add(request):
    login_id = request.session['logid']
    model_object = Product.objects.filter(comp_id=login_id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            ProductObj = form.cleaned_data
            name = ProductObj['product_name']
            rate = ProductObj['product_rate']
            description = ProductObj['product_description']
            image = ProductObj['product_image']

            a = Product(product_name=name, product_rate=rate, product_description=description, product_image=image,
                        comp_id=login_id)
            a.save()

            return redirect('producttemp:ProductForm')
    else:
        form = forms.ProductForm
    return render(request, "product/product.html", {'form': form, 'data': model_object, 'IDD': login_id})

