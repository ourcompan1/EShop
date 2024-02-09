from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/', views.index, name='index'),

    path('new_cars', views.new_cars, name='new_cars'),
    path('new_cars/', views.new_cars, name='new_cars'),

    path('contacts', views.contacts, name='contacts'),
    path('contacts/', views.contacts, name='contacts'),

    path('finance', views.finance, name='finance'),
    path('finance/', views.finance, name='finance'),


]