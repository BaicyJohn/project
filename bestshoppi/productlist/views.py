from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def listProduct(request):
    model_object = Product.objects.all()
    cnt=0
    return render(request, "productlist/productlist.html", {'data': model_object, 'cnt': cnt})
