from django.shortcuts import render, redirect
from . import forms


def product_add(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('product:ProductForm')
    else:
        form = forms.ProductForm

    return render(request, "product/product.html", {'form': form})
