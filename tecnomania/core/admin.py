from django.contrib import admin
from .models import CuentaUsuario
from .models import RegistroUsuario
from .models import TarjetaCredito


class CuentaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'contraseña')
admin.site.register(CuentaUsuario, CuentaUsuarioAdmin)



class RegistroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'nombre_usuario', 'nombres', 'apellidos', 'fecha_nacimiento', 'genero', 'numero_celular')
    list_display_links = ('id', 'correo')

admin.site.register(RegistroUsuario, RegistroUsuarioAdmin)

class TarjetaCreditoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'numero_tarjeta', 'expiracion_mes', 'expiracion_ano', 'cvc')

admin.site.register(TarjetaCredito, TarjetaCreditoAdmin)

