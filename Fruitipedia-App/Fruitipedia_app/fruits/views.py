from django.shortcuts import render, redirect
from Fruitipedia_app.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from Fruitipedia_app.fruits.models import Fruit
from Fruitipedia_app.profiles.models import Profile


def create_fruit_view(request):
    form = CreateFruitForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        fruit = form.save(commit=False)
        fruit.owner = Profile.objects.first()
        fruit.save()
        return redirect('dashboard')

    context = {'form': form}
    return render(request, 'fruits/create-fruit.html', context=context)


def details_fruit_view(request, fruitId):
    fruit = Fruit.objects.get(pk=fruitId)

    context = {'fruit': fruit}

    return render(request, 'fruits/details-fruit.html', context=context)


def edit_fruit_view(request, fruitId):
    fruit = Fruit.objects.get(pk=fruitId)
    form = EditFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {'form': form,
               'fruit': fruit}

    return render(request, 'fruits/edit-fruit.html', context=context)


def delete_fruit_view(request, fruitId):
    fruit = Fruit.objects.get(pk=fruitId)
    form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {'form': form, 'fruit': fruit}
    return render(request, 'fruits/delete-fruit.html', context=context)
