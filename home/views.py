from django.shortcuts import render

from products.models import Product


def index(request):
    """ A view to return the index/home page """
    products = Product.objects.all().order_by('-pk')[0:4]

    return render(request, 'home/index.html', {'products': products})
