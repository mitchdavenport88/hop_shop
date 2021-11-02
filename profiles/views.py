from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display profile (user specific) """
    get_user_profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': get_user_profile,
    }

    return render(request, 'profiles/profile.html', context)
