from os import name
from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('submit',views.tamilword)
]