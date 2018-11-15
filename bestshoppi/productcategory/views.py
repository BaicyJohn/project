from django.shortcuts import render, redirect
from .import forms


def product_category(request):
    if request.method == 'POST':
        form = forms.ProductCatForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Inserted Succesfully"
            return redirect('productcategory:ProductCatForm')
    else:
        form = forms.ProductCatForm
        msg = "Not inserted"
    return render(request, "productcategory/productcat.html", {'form': form, 'msg': msg})