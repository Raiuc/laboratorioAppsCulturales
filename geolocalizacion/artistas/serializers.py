from rest_framework import serializers

from artistas.models import Artista, Programador, Pieza, Sede, Registro

class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para modelo de Artista
    """

    class Meta:
        model   = Artista
        fields  = ('nombre', 'apellido_p', 'apellido_m', 'sexo', 'correo', 'nombre_artis',
                   'curriculum', 'nombre_com', 'cargo', 'semblanza', 'dir_usu', 'dir_com',
                   'foto_per', 'foto_com', 'red_soc_per', 'red_soc_com', 'web')


class ProgramadorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para modelo de Programador
    """

    class Meta:
        model   = Programador
        fields  = ('nombre' ,'apellido_p' ,'apellido_m')


class PiezaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para modelo de Pieza
    """
    artista             = ArtistaSerializer(many=False)
    programador         = ProgramadorSerializer(many=False)

    class Meta:
        model   = Pieza
        fields  = ('nombre', 'descripcion', 'tecnica', 'tipo_prod', 'disciplina',
                   'sinopsis', 'ano_creac', 'num_pers_prod', 'num_pers_tal', 'tipo_foro',
                   'aforo_obra', 'tipo_financ', 'foto_cartel', 'url_video', 'observaciones',
                   'artista', 'programador')


class SedeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para modelo de Sede
    """

    class Meta:
        model   = Sede
        fields  = ('nombre_sede','tipo_sede','address','geolocation')


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para modelo de Registro
    """
    pieza               = PiezaSerializer(many=False)
    programador         = ProgramadorSerializer(many=False)
    sede                = SedeSerializer(many=False)

    class Meta:
        model   = Registro
        fields  = ('pieza','programador','sede','financiamiento','ano_present',
                   'tipo_gestion','num_presen', 'fecha', 'comentarios')
