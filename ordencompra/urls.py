from django.urls import path
from . import views

urlpatterns = [
    path("", views.ordencompra, name="ordencompra"),
    path("importar-datos/", views.importar_datos, name="importar_datos"),
    # Puedes ajustar la URL según tus preferencias
]
