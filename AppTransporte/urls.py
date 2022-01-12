
from django.urls import path
from AppTransporte import views

urlpatterns = [
  
    path('inicio/', views.inicio, name="Inicio"),
    path('pasajero/', views.pasajero, name="Pasajero"),
    path('chofer/', views.chofer, name="Chofer"),
    path('transporte/', views.transporte, name="Transporte"),
    path('terminal/', views.terminal, name="Terminal"),
    path('pasajeroFormulario', views.pasajeroFormulario, name='PasajeroFormulario'),
    path('choferFormulario', views.choferFormulario),
    path('transporteFormulario', views.transporteFormulario),
    path('terminalFormulario', views.terminalFormulario, name='TerminalFormulario'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('chofer/list', views.ChoferList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ChoferDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ChoferCreacion.as_view(), name='New'),
    path(r'^editar(?P<pk>\d+)$', views.ChoferUpdate.as_view(), name='Edit'),
    path(r'^borrar(?P<pk>\d+)$', views.ChoferDelete.as_view(), name='Delete'),
    path('busquedaChofer', views.busquedaChofer),
    path('busquedaPasajero', views.busquedaPasajero),
    path('busquedaTerminal', views.busquedaTerminal),
    path('busquedaTransporte', views.busquedaTransporte),
    path('buscarChofer/', views.buscarChofer),
    path('buscarPasajero/', views.buscarPasajero),
    path('buscarTerminal/', views.buscarTerminal),
    path('buscarTransporte/', views.buscarTransporte),
    path('buscarTransporte/', views.buscarTransporte),
    path('leerPasajeros/', views.leerPasajeros, name='LeerPasajeros'),
    path('leerTerminales/', views.leerTerminales, name='LeerTerminales'),
    path('leerTransportes/', views.leerTransportes, name='LeerTransportes'),
    path('eliminarPasajero/<pasajero_nombre>/', views.eliminarPasajero, name='EliminarPasajero'),
    path('eliminarTerminal/<terminal_nombre>/', views.eliminarTerminal, name='EliminarTerminal'),
    path('editarPasajero/<pasajero_nombre>/', views.editarPasajero, name='EditarPasajero'),
    path('editarTerminal/<terminal_nombre>/', views.editarTerminal, name='EditarTerminal'),
]