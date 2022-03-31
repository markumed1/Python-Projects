from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import Person

def home(request):
    profiles = Person.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Person, pk=pk)
    form = ContactForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profiles.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context = {"item": item, }
    return render(request, 'profiles/confirmDelete.html', context)

def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('home')
    else:
        return redirect('home')


def createProfile(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/createProfile.html', context)