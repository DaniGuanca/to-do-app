from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='home'),
    path('agregarForm/', views.agregar_elemento),
    path('borrarItem/<int:elemento_id>/', views.borrar_elemento),
    #path('todo', views.todo, name='todo')
]