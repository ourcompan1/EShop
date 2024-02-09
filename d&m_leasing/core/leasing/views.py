from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'core/index.html')


def new_cars(request):
    cars = models.Car.objects.all()
    return render(request, 'core/new-cars.html', {'cars': cars})


def contacts(request):
    return render(request, 'core/contacts.html')


def finance(request):
    return render(request, 'core/finance.html')