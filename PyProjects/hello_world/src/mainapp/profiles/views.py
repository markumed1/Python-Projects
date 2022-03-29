from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def home(request):
    profiles = Person.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})