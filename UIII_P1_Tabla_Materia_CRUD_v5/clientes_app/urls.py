from django.urls import path
from materia_app import views
urlpatterns = [
    path("", views.inicio_vista, name= "inicio_vista" ),
    path("registrarClientes/",views.registrarMateria,name="registrarClientes"),
    path("seleccionarClientes/<codigo>",views.seleccionarMateria,name="seleccionarClientes"),
    path("editarClientes/",views.editarMateria,name="editarClientes"),
    path("borrarClientes/<codigo>",views.borrarMateria,name="borrarClientes")
]
