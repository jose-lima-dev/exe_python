from operator import imod
from django.urls import path
from app_cad_usuarios import views
from projeto_cad_usuarios.app_cad_usuarios.views import usuarios

urlpatterns = [
    # rota, view responsável, nome de referência
    #
    path('', views.home, name='home')
    path('usuarios/', views.usuarios, name='listagem_usuario')
]

