from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product


def full_list(request):
    all_products = Product.objects.all()
    return render(request, 'all_products.html', {'all_products': all_products})


