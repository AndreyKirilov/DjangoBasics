from django.shortcuts import render, redirect
from django.views.generic import CreateView

from Fruitipedia_app.profiles.models import Profile
from Fruitipedia_app.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


# Create your views here.

def create_profile_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = CreateProfileForm()

    return render(request, 'profiles/create-profile.html', {'form': form})


def details_profile_view(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'profiles/details-profile.html', context=context)


def edit_profile_view(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {'profile': profile,
               'form': form}

    return render(request, 'profiles/edit-profile.html', context=context)


def delete_profile_view(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {'profile': profile,
               'form': form}

    return render(request, 'profiles/delete-profile.html', context=context)
