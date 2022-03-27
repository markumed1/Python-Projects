from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Goku", "Vegeta", "Gohan", "Trunks", "Piccolo", "Chi Chi"]
    context = {
        'names': names,
    }
    return render(request, "home.html", context)