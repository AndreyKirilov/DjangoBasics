from django.shortcuts import render
from Fruitipedia_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'common/index.html', context=context)


def dashboard_view(request):
    profile = Profile.objects.first()
    fruits = profile.profile_fruits.all()

    context = {'profile': profile,
               'fruits': fruits}

    return render(request, 'common/dashboard.html', context=context)
