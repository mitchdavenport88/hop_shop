from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponseRedirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from profiles.models import UserProfile
from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to show all products """
    products = Product.objects.all().order_by('name')
    query = None
    category = None
    country = None
    sort = None
    direction = None

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        user_profile = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)

        if 'country' in request.GET:
            country = request.GET['country']
            products = products.filter(country__name=country)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    country__name__icontains=query) | Q(
                        category__friendly_name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_query': query,
        'current_sorting': current_sorting,
        'user_profile': user_profile,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual products """
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        user_profile = None

    context = {
        'product': product,
        'user_profile': user_profile,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ A view to add products to the store """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Hop Shop Admin have \
            access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Check the \
                form is valid and try again.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ A view to edit products in the store """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Hop Shop Admin have \
            access to this page!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Check the \
                form is valid and try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}.')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ A view that deletes a selected product from the store """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Hop Shop Admin have \
            access to this page!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def wishlist(request):
    """ A view to show all products that are on a users wishlist """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    wishlist_products = user_profile.wishlist.all()

    context = {
        'user_profile': user_profile,
        'wishlist_products': wishlist_products,
    }

    return render(request, 'products/wishlist.html', context)


# Code for the wishlist toggle function was found on the following video
# and edited accordingly - https://www.youtube.com/watch?v=OgA0TTKAtqQ&t=2403s
@login_required
def wishlist_toggle(request, product_id):
    """
    A view that adds and removes (toggles) products to the users wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if user_profile.wishlist.filter(pk=product_id).exists():
        user_profile.wishlist.remove(product)
        messages.info(request, f'{product.name} removed from wishlist!')
    else:
        user_profile.wishlist.add(product)
        messages.info(request, f'{product.name} added to wishlist!')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
