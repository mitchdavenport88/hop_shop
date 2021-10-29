from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There\'s nothing in your cart currently')
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdBkIFZyCWoSHERmnXfDSsfSGJclc6paQqPH2oY4rvNm2ahaY6MdCvPC1T7zQ4d6XTAJETpf2AGzoNBWZ2hGlWR00xvkCE8sk',
        'client_secret': 'test',
    }

    return render(request, 'checkout/checkout.html', context)
