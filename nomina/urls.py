from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # <-- página de inicio
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),

    # rutas de nómina...
    path('nominas/', views.lista_nominas, name='lista_nominas'),
    path('nominas/crear/', views.crear_nomina, name='crear_nomina'),
    path('nominas/editar/<int:pk>/', views.editar_nomina, name='editar_nomina'),
    path('nominas/eliminar/<int:pk>/', views.eliminar_nomina, name='eliminar_nomina'),
    path('nominas/<int:pk>/detalles/', views.detalles_nomina, name='detalles_nomina'),
    path('nominas/<int:pk>/agregar-detalle/', views.agregar_detalle_nomina, name='agregar_detalle_nomina'),
]
