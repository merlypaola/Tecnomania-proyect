from django.shortcuts import render, redirect
from .models import CuentaUsuario, RegistroUsuario, TarjetaCredito
from django.contrib import messages
import random
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse



def index(request):
    return render(request, "core/index.html")

def cuenta(request):
    return render(request, "core/cuenta.html")

def registro(request):
    return render(request, "core/registro.html")


def pago(request):
    return render(request, "core/pago.html")


def tecnomania(request):
    return render(request, "core/tecnomania.html")

def cuentausuario_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')  # Nombre del input en el formulario HTML
        contraseña = request.POST.get('contraseña')  # Nombre del input en el formulario HTML
        cuenta = CuentaUsuario(correo=correo, contraseña=contraseña)
        cuenta.save()
        
    return render(request, 'core/cuenta.html')


def registrar_cuenta_view(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        numero_celular = request.POST.get('numero_celular')
        correo = request.POST.get('correo')
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')
        validar_contraseña = request.POST.get('validar_contraseña')  # Obtén la validación de contraseña

        # Verifica si las contraseñas coinciden
        if contraseña == validar_contraseña:
            registro = RegistroUsuario(
                nombres=nombres,
                apellidos=apellidos,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                numero_celular=numero_celular,
                correo=correo,
                nombre_usuario=nombre_usuario,
                contraseña=contraseña
            )
            registro.save()
            return redirect('cuenta')  
        else:
          
             error_message = "Las contraseñas no coinciden. Por favor, inténtalo nuevamente O Ingrese nuevamente su contraseña"
            
        
    return render(request, 'core/crear_cuenta.html', {'error_message': error_message})


@csrf_protect
def tarjeta_credito_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        expiracion_mes = request.POST.get('expiracion_mes')
        expiracion_ano = request.POST.get('expiracion_ano')
        cvc = request.POST.get('cvc')

        pago_exitoso = random.choice([True, False])

        if pago_exitoso:
            tarjeta = TarjetaCredito(
                nombre=nombre,
                numero_tarjeta=numero_tarjeta,
                expiracion_mes=expiracion_mes,
                expiracion_ano=expiracion_ano,
                cvc=cvc
            )
            tarjeta.save()
            JsonResponse({'status': 'success', 'message': 'Tarjeta de crédito guardada exitosamente.'})
        else:
             return JsonResponse({'status': 'error', 'message': 'Error al procesar la tarjeta de crédito. Inténtalo nuevamente.'})

    return render(request, 'core/pago.html')
