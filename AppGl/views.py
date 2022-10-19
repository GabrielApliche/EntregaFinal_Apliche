from django.shortcuts import render
from AppGl.models import *
from AppGl.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#Página Principal 
def inicio(request):
    return render(request, "AppGl/inicio.html")

#Página de Recetas
@login_required
def receta(request):
    recetas = Receta.objects.all()
    return render(request, "AppGl/Recetas/listaReceta.html", {"resultados":recetas})

def about(request):
    return render(request, "AppGl/about.html")

#Vista para registrarse
def registro(request):

    if request.method == "POST":    

        form = RegistroFormulario(request.POST)   

        if form.is_valid():

            user=form.cleaned_data["username"]
            form.save()
            
            return render(request, "AppGl/inicio.html", {"mensaje":"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   
    
    
    return render(request, "AppGl/Autenticar/registro.html", {"form":form})

#Vista para iniciar sesión
def login_request(request):

    if request.method == "POST": 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get("username")   
            contra=form.cleaned_data.get("password")    

            user=authenticate(username=usuario, password=contra)    

            if user:    

                login(request, user)   

                return render(request, "AppGl/inicio.html", {"mensaje":f"Bienvenido {user}"}) 

        else:   
    
            return render(request, "AppGl/inicio.html", {"mensaje":"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "AppGl/Autenticar/login.html", {"form":form})    

#Vista para Editar Usuarios
@login_required
def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     

            usuario.username = informacion["username"]
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password1"]
            usuario.save()

            return render(request, "AppGl/inicio.html")

    else:

        miFormulario = RegistroFormulario(initial={"username":usuario.username, "email":usuario.email})

    return render(request, "AppGl/Autenticar/editarUser.html",{"miFormulario":miFormulario, "usuario":usuario.username})


#Agregar Receta
@login_required
def recetaFormulario(request):

    if request.method == "POST":

        Formulario1=RecetaFormulario(request.POST, request.FILES)

        if Formulario1.is_valid():

            info = Formulario1.cleaned_data

            receta = Receta(imagen=info["imagen"], nombre=info["nombre"], ingredientes=info["ingredientes"], tiempo=info["tiempo"], preparacion=info["preparacion"])

            receta.save()

            return render(request, "AppGl/inicio.html")
    else:

        Formulario1=RecetaFormulario()

    return render(request, "AppGl/Recetas/añadirReceta.html", {"form":Formulario1})

#Borrar Receta
@login_required
def borrarReceta(request, receta_nombre):

    recet = Receta.objects.get(nombre=receta_nombre)
    
    recet.delete()
    
    recetas = Receta.objects.all()

    return render(request, "AppGl/Recetas/listaReceta.html",{"resultados":recetas})

#Editar Receta
@login_required
def editarReceta(request, receta_nombre):

    recet = Receta.objects.get(nombre=receta_nombre)

    if request.method == "POST":

        miFormulario = EditarReceta(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            recet.imagen = informacion["imagen"]
            recet.nombre = informacion["nombre"]
            recet.ingredientes = informacion["ingredientes"]
            recet.tiempo = informacion["tiempo"]
            recet.preparacion = informacion["preparacion"]

            recet.save()

            return render(request, "AppGl/inicio.html")

    else:

        miFormulario= EditarReceta(initial={"nombre":recet.nombre, "ingredientes":recet.ingredientes, "tiempo":recet.tiempo, "preparacion":recet.preparacion})

    return render(request, "AppGl/Recetas/editarReceta.html", {"miFormulario":miFormulario, "resultado":receta_nombre})

#Vista de Busqueda
@login_required
def buscarReceta(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        recetas = Receta.objects.filter(nombre__icontains=nombre)

        return render(request, "AppGl/Recetas/resultadoBusqueda.html",{"recetas":recetas, "nombre":nombre})

    else:

        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)
