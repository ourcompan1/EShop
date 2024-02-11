from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/', views.index, name='index'),

    path('new_cars', views.new_cars, name='new_cars'),
    path('new_cars/', views.new_cars, name='new_cars'),

    path('new_cars/lvsb', views.lease_vs_buy, name='l_vs_b'),
    path('new_cars/lvsb/', views.lease_vs_buy, name='l_vs_b'),

    path('contacts', views.contacts, name='contacts'),
    path('contacts/', views.contacts, name='contacts'),

    path('finance', views.finance, name='finance'),
    path('finance/', views.finance, name='finance'),


]