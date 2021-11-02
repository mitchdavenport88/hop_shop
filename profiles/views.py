from django.shortcuts import render


def profile(request):
    """ Display profile (user specific) """

    context = {}

    return render(request, 'profiles/profile.html', context)
