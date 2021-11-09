from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display profile (user specific) """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery information updated.')
        else:
            messages.error(request, 'Delivery information update failed.')
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all().order_by('-date')
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past order confirmation for order no. {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
