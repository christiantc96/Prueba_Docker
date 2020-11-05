from django.contrib import admin  
from django.urls import path  
from Oit import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('agregar', views.agregar, name="agregar_oit"),  
    path('mostrar',views.mostrar, name="mostrar_oit"),  
    path('editar/<int:id>', views.editar, name="editar_oit"),  
    path('actualizar/<int:id>', views.actualizar, name="actualizar_oit"),  
    path('eliminar/<int:id>', views.eliminar, name="eliminar_oit"),  
]  