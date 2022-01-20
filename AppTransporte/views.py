from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

from AppTransporte.models import Chofer, Pasajero, Transporte, Terminal
from AppTransporte.forms import ChoferFormulario, PasajeroFormulario, TransporteFormulario, TerminalFormulario, UserRegisterForm, UserEditForm


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required




def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppTransporte/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppTransporte/register.html" ,  {"form":form})



def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppTransporte/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppTransporte/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppTransporte/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppTransporte/login.html", {'form':form} )



@login_required
def editarPerfil(request):
        
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "AppTransporte/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppTransporte/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

                        



class ChoferList(ListView):
    
    model = Chofer
    template_name = "AppTransporte/chofer_list.html"

#Detalle - SUPER Leer - Buscar!!!!!
class ChoferDetalle(DetailView):
    
    model = Chofer
    template_name = "AppTransporte/chofer_detalle.html"
    
#Crear elementos
class ChoferCreacion(CreateView):
    
    model = Chofer
    success_url = "../AppTransporte/chofer/list"
    fields = ["nombre", "apellido", "numeroDeDocumento","numeroDeLicencia"]
    
#modificar!!!!!!!!!!!  
class ChoferUpdate(UpdateView):
    
    model = Chofer
    success_url = "../chofer/list"
    fields = ["nombre", "apellido", "numeroDeDocumento","numeroDeLicencia"]
  
#Borrar   
class ChoferDelete(DeleteView):
    
    model = Chofer
    success_url = "../chofer/list"
      






class PasajeroList(ListView):
    
    model = Pasajero
    template_name = "AppTransporte/pasajero_list.html"

#Detalle - SUPER Leer - Buscar!!!!!
class PasajeroDetalle(DetailView):
    
    model = Pasajero
    template_name = "AppTransporte/pasajero_detalle.html"
    
#Crear elementos
class PasajeroCreacion(CreateView):
    
    model = Pasajero
    success_url = "../AppTransporte/pasajero/list" 
    fields = ["nombre", "apellido", "numeroDeDocumento","vacunado"]
    
#modificar!!!!!!!!!!!  
class PasajeroUpdate(UpdateView):
    
    model = Pasajero
    success_url = "../pasajero/list"
    fields = ["nombre", "apellido", "numeroDeDocumento","vacunado"]
  
#Borrar   
class PasajeroDelete(DeleteView):
    
    model = Pasajero
    success_url = "../pasajero/list"




def choferFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ChoferFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            chofer = Chofer(
                
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                numeroDeDocumento = informacion['numeroDeDocumento'],
                numeroDeLicencia = informacion['numeroDeLicencia']     
                
            )
            
            chofer.save()
            
            return render(request, 'AppTransporte/inicio.html')
        
    else:
        
        miFormulario = ChoferFormulario()
    
    return render(request, 'AppTransporte/choferFormulario.html', {"miFormulario":miFormulario})





  
def pasajeroFormulario(request):
        
      if request.method == 'POST':

            miFormulario = PasajeroFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pasajero = Pasajero (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], vacunado=informacion['vacunado']) 

                  pasajero.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PasajeroFormulario() #Formulario vacio para construir el html
 
      return render(request, "AppTransporte/pasajeroFormulario.html", {"miFormulario":miFormulario})
  
def transporteFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TransporteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  transporte = Transporte (tipo=informacion['tipo'], empresa=informacion['empresa'], capacidad=informacion['capacidad'], patente=informacion['patente']) 

                  transporte.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TransporteFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/transporteFormulario.html", {"miFormulario":miFormulario})
  
def terminalFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TerminalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  terminal = Terminal (nombre=informacion['nombre'], ubicacion=informacion['ubicacion']) 

                  terminal.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TerminalFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/terminalFormulario.html", {"miFormulario":miFormulario})  




# Create your views here.
def inicio(request):
    return render(request, "AppTransporte/inicio.html")
    
def pasajero(request):
    return render(request, "AppTransporte/pasajero.html")

def chofer(request):
    return render(request, "AppTransporte/chofer.html")

def transporte(request):
    return render(request, "AppTransporte/transporte.html")

def terminal(request):
    return render(request, "AppTransporte/terminal.html")

def busquedaChofer(request):

      return render(request, "AppTransporte/busquedaChofer.html")

def busquedaPasajero(request):

      return render(request, "AppTransporte/busquedaPasajero.html")

def busquedaTerminal(request):

      return render(request, "AppTransporte/busquedaTerminal.html")

def busquedaTransporte(request):

      return render(request, "AppTransporte/busquedaTransporte.html")





def buscarChofer(request):
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        chofer = Chofer.objects.filter(nombre__icontains=nombre)
        
               
        #respuesta = f"Estoy Buscando a : {request.GET['nombre']} "
        
        return render(request, "AppTransporte/resultadoChofer.html", {"chofer":chofer, "nombre":nombre} )
        
        
    else:
        
        repuesta = "Che, mandame informacion!!"
    
    return HttpResponse(respuesta)




def buscarPasajero(request):
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            pasajero=Pasajero.objects.filter(nombre__icontains=nombre)

            return render(request, "AppTransporte/resultadoPasajero.html",{"pasajero":pasajero,"nombre":nombre})

      else:
            respuesta="no enviaste datos"

      return HttpResponse(respuesta)  

def buscarTerminal(request):
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            terminal=Terminal.objects.filter(nombe__icontains=nombre)

            return render(request, "AppTransporte/resultadoTerminal.html",{"nombre":nombre, "ubicacion":ubicacion})

      else:
            respuesta="no enviaste datos"

      return HttpResponse(respuesta)  

def buscarTransporte(request):
      if request.GET["empresa"]:
            empresa=request.GET['empresa']
            empresa= Empresa.objects.filter(nombe__icontains=empresa)

            return render(request, "AppTransporte/resultadoTransporte.html",{"tipo":tipo, "empresa":empresa,"capacidad":capacidad, "patente":patente})

      else:
            respuesta="no enviaste datos"

      return HttpResponse(respuesta)       



#Armado de CRUD 
# 1ro 


@login_required
def leerChoferes(request):
    
    choferes = Chofer.objects.all()
    
    dir = {"choferes":choferes} #contexto
    
    return render(request, "AppTransporte/leerChoferes.html", dir)


def leerPasajeros(request):

      pasajeros=Pasajero.objects.all()
      contexto= {"pasajeros":pasajeros}

      return render(request, "AppTransporte/leerPasajeros.html",contexto)               

def leerTerminales(request):

      terminales=Terminal.objects.all()
      contexto= {"terminales":terminales}

      return render(request, "AppTransporte/leerterminales.html",contexto) 

def leerTransportes(request):

      transportes=Transporte.objects.all()
      contexto= {"transporte":transportes}

      return render(request, "AppTransporte/leertransportes.html",contexto)   




#2do
def eliminarChofer(request, chofer_nombre):

      chofer=Chofer.objects.get(nombre=chofer_nombre)
      chofer.delete()

      choferes=Chofer.objects.all()
      contexto={"choferes":choferes}

      return render(request, "AppTransporte/leerChoferes.html",contexto)

def eliminarPasajero(request, pasajero_nombre):

      pasajero=Pasajero.objects.get(nombre=pasajero_nombre)
      pasajero.delete()

      pasajeros=Pasajero.objects.all()
      contexto={"pasajeros":pasajeros}

      return render(request, "AppTransporte/leerPasajeros.html",contexto)           

def eliminarTerminal(request, terminal_nombre):

      terminal=Terminal.objects.get(nombre=terminal_nombre)
      terminal.delete()

      terminales=Terminal.objects.all()
      contexto={"terminales":terminales}

      return render(request, "AppTransporte/leerTerminales.html",contexto)



#3ro
def editarChofer(request, chofer_nombre):

      chofer= Chofer.objects.get(nombre=chofer_nombre)
        
      if request.method == 'POST':

            miFormulario = ChoferFormulario(request.POST) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  
                  chofer.nombre = informacion["nombre"]
                  chofer.apellido = informacion["apellido"]
                  chofer.numeroDeDocumento = informacion["numeroDeDocumento"]
                  chofer.numeroDeLicencia = informacion["numeroDeLicencia"]
                                

                  chofer.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ChoferFormulario(initial={"nombre":chofer.nombre, "apellido":chofer.apellido, "numeroDeDocumento":chofer.numeroDeDocumento, "numeroDeLicencia":chofer.numeroDeLicencia}) #Formulario vacio para construir el html
 
      return render(request, "AppTransporte/editarChofer.html", {"miFormulario":miFormulario, "chofer_nombre":chofer_nombre}) 


def editarPasajero(request, pasajero_nombre):

      pasajero= Pasajero.objects.get(nombre=pasajero_nombre)
        
      if request.method == 'POST':

            miFormulario = PasajeroFormulario(request.POST) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  
                  pasajero.nombre = informacion["nombre"]
                  pasajero.apellido = informacion["apellido"]
                  pasajero.numeroDeDocumento = informacion["numeroDeDocumento"]
                  pasajero.vacunado = informacion["vacunado"]
                                

                  pasajero.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PasajeroFormulario(initial={"nombre":pasajero.nombre, "apellido":pasajero.apellido, "numeroDeDocumento":pasajero.numeroDeDocumento, "vacunado":pasajero.vacunado}) #Formulario vacio para construir el html
 
      return render(request, "AppTransporte/editarPasajero.html", {"miFormulario":miFormulario, "pasajero_nombre":pasajero_nombre})      

def editarTerminal(request, terminal_nombre):
      terminal=Terminal.objects.get(nombre=terminal_nombre)  
      if request.method == 'POST':

            miFormulario = TerminalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  terminal = Terminal (nombre=informacion['nombre'], ubicacion=informacion['ubicacion']) 

                  terminal.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TerminalFormulario(initial={'nombre':terminal.nombre,'ubicacion':terminal.ubicacion}) #Formulario vacio para construir el html

      return render(request, "AppTransporte/editarTerminal.html", {"miFormulario":miFormulario, "terminal_nombre":terminal_nombre})           
      