"""
URL configuration for tecnomania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from django.contrib import admin
from core import views



urlpatterns = [
    path('', views.index, name='index'),
    path('cuenta/', views.cuenta, name="cuenta"),
    path('registro/', views.registro, name="registro"),
    path('pago/', views.pago, name="pago"),  # Cambio de 'compra' a 'pago'
    path('tecnomania/', views.tecnomania, name="tecnomania"),
    path('admin/', admin.site.urls),
    path('crear-cuenta/', views.cuentausuario_view, name='cuentausuario'),
    path('registrar-cuenta/', views.registrar_cuenta_view, name='registrar_cuenta'),
    path('tarjeta_credito/', views.tarjeta_credito_view, name='tarjeta_credito'),

]
