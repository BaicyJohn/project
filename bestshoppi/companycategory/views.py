from django.shortcuts import render, redirect
from .import forms


def comp_category(request):
    if request.method == 'POST':
        form = forms.CompCatForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Inserted Succesfully"
            return redirect('companycategory:CompCatForm')
    else:
        form = forms.CompCatForm
        msg = "Not inserted"
    return render(request, "company_category/comp_category.html", {'form': form, 'msg': msg})