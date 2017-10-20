from django.contrib import admin
from artistas.models import Artista, Lugar, Pieza, Programador, Coleccionista

admin.site.register(Artista)
admin.site.register(Lugar)
admin.site.register(Programador)
admin.site.register(Coleccionista)
admin.site.register(Pieza)

# Register your models here.
