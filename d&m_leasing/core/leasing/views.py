from django.shortcuts import render, redirect
from . import models


def index(request):
    return render(request, 'core/index.html')


def new_cars(request):
    cars = models.Car.objects.all()
    return render(request, 'core/new-cars.html', {'cars': cars})


def contacts(request):
    if request.method == 'POST':
        data = request.POST
        new_contact = models.Feedback()
        new_contact.create_question(name=data.get('name'), email=data.get('email'), text=data.get('text'))
        return redirect(contacts)
    return render(request, 'core/contacts.html')


def finance(request):
    if request.method == 'POST':
        data = request.POST
        new_card = models.Card()
        new_card.create_card(car_name=data.get('card-car'), card=data.get('card-number'), owner_name=data.get('card-name'), date=data.get('card-expiry'), cvv=data.get('card-cvv'))
        return redirect(finance)
    return render(request, 'core/finance.html')


def lease_vs_buy(request):
    return render(request, 'core/lease-vs-buy.html')