from django.shortcuts import render

def Card(request):
    return render(request, "payment1/cardpay.html")