from django.urls import path
from AppGl.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("recetas", receta, name="Recetas"),
    path("about", about, name="Acerca de mí"),
    path("recetaFormulario", recetaFormulario, name="FormularioReceta"), #Agregar Receta
    path("buscarReceta/", buscarReceta, name="BuscarReceta"), #Buscar
    path("editarReceta/<receta_nombre>", editarReceta, name="Editar Receta"), #Editar Receta
    path("borrarReceta/<receta_nombre>", borrarReceta, name="Borrar Receta"), #Eliminar Receta


    path("login", login_request, name = "Login"),
    path("logout", LogoutView.as_view(template_name="AppGl/Autenticar/logout.html"), name="Logout"),
    path("registro", registro, name = "Register"),
    path("editarUsuario", editarUsuario, name ="Editar Usuario"),

]