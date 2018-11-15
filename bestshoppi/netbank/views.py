from django.shortcuts import render


def netbank(request):
    return render(request, "payment/NetBanking.html")




