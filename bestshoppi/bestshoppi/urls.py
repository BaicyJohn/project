"""bestshoppi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^custreg/', include('custregisteration.urls')),
    url(r'^custlogin/', include('customerlogin.urls')),
    url(r'^compcategory/', include('companycategory.urls')),
    url(r'^complogin/', include('companylogin.urls')),
    url(r'^productadd/', include('products.urls')),
    url(r'^productcat/', include('productcategory.urls')),
   # url(r'^product/', include('producttemp.urls')),
    url(r'^compfeedback/', include('productfeedback.urls')),
    url(r'^compreg/', include('companyregisteration.urls')),
    url(r'^profile/', include('companyprofile.urls')),
    url(r'^custprofile/', include('customerprofile.urls')),
    url(r'^productlist/', include('productlist.urls')),
    url(r'^quantity/', include('quantity.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^total/', include('totalrate.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^card/', include('card.urls')),
    url(r'^netbank/', include('netbank.urls')),
    url(r'^finalpay/', include('finalpay.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^adminlogin/', include('adminlogin.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
