from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppTransporte.models import Chofer, Pasajero, Transporte, Terminal
from AppTransporte.forms import ChoferFormulario, PasajeroFormulario, TransporteFormulario, TerminalFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

                        



class ChoferDelete(DeleteView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"

class ChoferUpdate(UpdateView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'numeroDeLicencia']


class ChoferCreacion(CreateView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'numeroDeLicencia']

class ChoferDetalle(DetailView):

      model = Chofer
      template_name = "AppTransporte/chofer_detalle.html"

class ChoferList(ListView):

      model = Chofer
      template_name = "AppTransporte/chofer_list.html"



def choferFormulario(request):
    
      if request.method == 'POST':

            miFormulario = ChoferFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  chofer = Chofer (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], numeroDeLicencia=informacion['numeroDeLicencia']) 

                  chofer.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ChoferFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/choferFormulario.html", {"miFormulario":miFormulario})
  
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
            nombre=request.GET['nombre']
            chofer=Chofer.objects.filter(nombe__icontains=nombre)

            return render(request, "AppTransporte/resultadoChofer.html",{"nombre":nombre, "apellido":apellido,"dni":numeroDeDocumento,"licencia":numeroDeLicencia})

      else:
            respuesta="no enviaste datos"

      return HttpResponse(respuesta)   

def buscarPasajero(request):
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            pasajero=Pasajero.objects.filter(nombe__icontains=nombre)

            return render(request, "AppTransporte/resultadoPasajero.html",{"nombre":nombre, "apellido":apellido,"dni":numeroDeDocumento,"vacunado":vacunado})

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

def editarPasajero(request, pasajero_nombre):

      pasajero= Pasajero.objects.get(nombre=pasajero_nombre)
        
      if request.method == 'POST':

            miFormulario = PasajeroFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pasajero = Pasajero (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], vacunado=informacion['vacunado']) 

                  pasajero.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PasajeroFormulario(initial={'nombre':pasajero.nombre, 'apellido':pasajero.apellido, 'numeroDeDocumento':pasajero.numeroDeDocumento, 'vacunado':pasajero.vacunado}) #Formulario vacio para construir el html
 
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
      