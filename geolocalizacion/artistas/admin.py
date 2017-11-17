from django.contrib import admin
from artistas.models import Artista, Sede, Pieza, Programador, Coleccionista
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


class SedeAdmin(admin.ModelAdmin):
   formfield_overrides = {
       map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
}

admin.site.register(Artista)
admin.site.register(Sede, SedeAdmin)
admin.site.register(Programador)
admin.site.register(Coleccionista)
admin.site.register(Pieza)
