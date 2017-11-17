from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.utils import timezone

def index(request):
    """
    index
    """
    template = loader.get_template('index.html')
    context = {

    }

    return HttpResponse(template.render(context, request))
