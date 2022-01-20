
from django.urls import path
from AppTransporte import views

#para el logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
  
    path('inicio/', views.inicio, name="Inicio"),
    path('pasajero/', views.pasajero, name="Pasajero"),
    path('chofer/', views.chofer, name="Chofer"),
    path('transporte/', views.transporte, name="Transporte"),
    path('terminal/', views.terminal, name="Terminal"),
    
    
    path('pasajeroFormulario', views.pasajeroFormulario, name='PasajeroFormulario'),
    path('choferFormulario', views.choferFormulario, name='ChoferFormulario'),
    path('transporteFormulario', views.transporteFormulario),
    path('terminalFormulario', views.terminalFormulario, name='TerminalFormulario'),
    
    
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppTransporte/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    
    
    
    path('chofer/list', views.ChoferList.as_view(), name='List Chofer'),
    path(r'^(?P<pk>\d+)$', views.ChoferDetalle.as_view(), name='Detail Chofer'),    
    path(r'^nuevo$Chofer', views.ChoferCreacion.as_view(), name='New Chofer'),
    path(r'^editarChofer/(?P<pk>\d+)$', views.ChoferUpdate.as_view(), name='Edit Chofer'),
    path(r'^borrarChofer/(?P<pk>\d+)$', views.ChoferDelete.as_view(), name='Delete Chofer'),
    
    
    path('pasajero/list', views.PasajeroList.as_view(), name='List Pasajero'),
    path(r'^(?P<pk>\d+)$', views.PasajeroDetalle.as_view(), name='Detail Pasajero'),    
    path(r'^nuevo$Pasajero', views.PasajeroCreacion.as_view(), name='New Pasajero'),
    path(r'^editarPasajero/(?P<pk>\d+)$', views.PasajeroUpdate.as_view(), name='Edit Pasajero'),
    path(r'^borrarPasajero/(?P<pk>\d+)$', views.PasajeroDelete.as_view(), name='Delete Pasajero'),
    
    
    
    path('busquedaChofer', views.busquedaChofer),
    path('busquedaPasajero', views.busquedaPasajero),
    path('busquedaTerminal', views.busquedaTerminal),
    path('busquedaTransporte', views.busquedaTransporte),
    path('buscarChofer/', views.buscarChofer),
    path('buscarPasajero/', views.buscarPasajero),
    path('buscarTerminal/', views.buscarTerminal),
    path('buscarTransporte/', views.buscarTransporte),
    path('buscarTransporte/', views.buscarTransporte),
    
    
    path('leerChoferes/', views.leerChoferes, name='LeerChoferes'),
    path('leerPasajeros/', views.leerPasajeros, name='LeerPasajeros'),
    path('leerTerminales/', views.leerTerminales, name='LeerTerminales'),
    path('leerTransportes/', views.leerTransportes, name='LeerTransportes'),
    
    
    path('eliminarChofer/<chofer_nombre>/', views.eliminarChofer, name='EliminarChofer'),
    path('eliminarPasajero/<pasajero_nombre>/', views.eliminarPasajero, name='EliminarPasajero'),
    path('eliminarTerminal/<terminal_nombre>/', views.eliminarTerminal, name='EliminarTerminal'),
    
    
    path('editarChofer/<chofer_nombre>/', views.editarChofer, name='EditarChofer'),
    path('editarPasajero/<pasajero_nombre>/', views.editarPasajero, name='EditarPasajero'),
    path('editarTerminal/<terminal_nombre>/', views.editarTerminal, name='EditarTerminal'),
]