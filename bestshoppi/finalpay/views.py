from django.shortcuts import render


def finalpay(request):
    return render(request, "payment/FinalPage.html")
