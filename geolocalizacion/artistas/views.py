from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.utils import timezone

from rest_framework import routers, serializers, viewsets

from artistas.models import Artista, Programador, Pieza, Sede, Registro
from artistas.serializers import ArtistaSerializer, ProgramadorSerializer, PiezaSerializer, SedeSerializer, RegistroSerializer

def index(request):
    """
    index
    """
    template = loader.get_template('index.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


class ArtistasListView(ListView):
    """
    Vista Simple para mostrar artistas
    """
    template_name = 'index.html'
    model = Artista
    queryset = Artista.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArtistasListView, self).get_context_data(**kwargs)
        context['now']=timezone.now()
        return context


# Classes para representación de API
class ArtistaListViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar artistas
    """
    queryset          = Artista.objects.all()
    serializer_class  = ArtistaSerializer


class ProgramadorListViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar programadores
    """
    queryset          = Programador.objects.all()
    serializer_class  = ProgramadorSerializer


class PiezaListViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar piezas
    """
    queryset          = Pieza.objects.all()
    serializer_class  = PiezaSerializer


class SedeListViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar artistas
    """
    queryset          = Sede.objects.all()
    serializer_class  = SedeSerializer


class RegistroListViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar registros
    """
    queryset          = Registro.objects.all()
    serializer_class  = RegistroSerializer
