from django.shortcuts import render, get_object_or_404
from django.contrib import messages

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

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)
