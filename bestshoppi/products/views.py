from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
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
            productcat = ProductObj['productcat_id']
            a = Product(product_name=name, product_rate=rate, product_description=description, product_image=image,
                        comp_id=login_id, productcat_id=productcat)
            a.save()
            pro_obj=Product.objects.last()
            idd= pro_obj.id
            messages.info(request, idd)


            return redirect('products:ProductForm')
    else:
        form = forms.ProductForm
    return render(request, "product/product.html", {'form': form, 'data': model_object})

def edit_product(request, pk):
    template = 'product/product.html'
    post = get_object_or_404(Product, pk=pk)
    model_object = Product.objects.all()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('products:ProductForm')

    else:
        form = forms.ProductForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }

    return render(request, template, context)
def delete_product(request, pk):
    post = get_object_or_404(Product, pk=pk)
    post.delete()
    return redirect('products:ProductForm')
