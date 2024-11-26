"""
URL configuration for sistema_assistencia_tecnica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cliente.views import ClienteView,cliente_view
from pecas.views import PecasView,pecas_view

rotas = routers.DefaultRouter()
rotas.register(r'cliente', ClienteView),
rotas = routers.DefaultRouter()
rotas.register(r'pecas', PecasView),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls)),
    path('cliente/',cliente_view, name='cliente'),
    path('pecas/', pecas_view,name='pecas'),
]