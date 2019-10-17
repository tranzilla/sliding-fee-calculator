from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #map the view in calc
    path('results', views.results, name ='results') #(name in url, linked to template, link to funct in views.py)

]
