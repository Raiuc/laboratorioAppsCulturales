"""geolocalizacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from artistas import views as a_views
from artistas.serializers import ArtistaSerializer, ProgramadorSerializer, PiezaSerializer, SedeSerializer, RegistroSerializer


"""
Routers: for automatically determining the URL conf.
"""
router = routers.DefaultRouter()
#api-auth
#modelosartistas
router.register(r'artista', a_views.ArtistaListViewSet)
router.register(r'programador', a_views.ProgramadorListViewSet)
router.register(r'pieza', a_views.PiezaListViewSet)
router.register(r'sede', a_views.SedeListViewSet)
router.register(r'registro', a_views.RegistroListViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', a_views.index),
    url(r'^mapa$', a_views.ArtistasListView.as_view(),name='mapa_artistas'),
    url(r'^', include(router.urls))
]
