from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import SlidingScale

# Create your views here.
def index(request):
    data = SlidingScale.objects.all()
    return TemplateResponse(request, 'calculator.html', {'data': data})


def results(request):
    return TemplateResponse(request, 'results.html', {})
