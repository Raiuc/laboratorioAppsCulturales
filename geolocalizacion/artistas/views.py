from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.utils import timezone
from artistas.models import Artista

def index(request):
    """
    index
    """
    template = loader.get_template('index.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


class ArtistasListView(ListView):
    """"""
    """"""
    template_name = 'index.html'
    model = Artista
    queryset = Artista.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ArtistasListView, self).get_context_data(**kwargs)
        context['now']=timezone.now()
        return context
    