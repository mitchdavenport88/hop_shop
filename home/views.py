from django.shortcuts import render, get_object_or_404

from products.models import Product
from profiles.models import UserProfile


def index(request):
    """ A view to return the index/home page """
    products = Product.objects.all().order_by('-pk')[0:4]

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        user_profile = None

    context = {
        'products': products,
        'user_profile': user_profile,
    }

    return render(request, 'home/index.html', context)
