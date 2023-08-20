from django.db import models


# Create your models here.

class CuentaUsuario(models.Model):
    correo = models.EmailField()
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.correo
    
class RegistroUsuario(models.Model):
    GENDER_CHOICES = [
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('No especificar', 'No especificar'),
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20, choices=GENDER_CHOICES)
    numero_celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.correo


class TarjetaCredito(models.Model):
    nombre = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    expiracion_mes = models.PositiveIntegerField()
    expiracion_ano = models.PositiveIntegerField()
    cvc = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.nombre} - {self.numero_tarjeta[-4:]}"

    
