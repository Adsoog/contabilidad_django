from django.urls import path
from . import views
from .views import crear_orden_venta
from .views import odventa, borrar_orden

urlpatterns = [
    path("", views.home, name="home"),
    path("ofventa/", views.ofventa, name="ofventa"),
    path("odventa/", views.odventa, name="odventa"),
    path("odcompra/", views.odcompra, name="odcompra"),
    path("inventario/", views.inventario, name="inventario"),
    path(
        "procesar_inventario_excel/",
        views.procesar_inventario_excel,
        name="procesar_inventario_excel",
    ),
    path(
        "procesar_ordenventa_excel/",
        views.procesar_ordenventa_excel,
        name="procesar_ordenventa_excel",
    ),
    path("crear_orden_venta/", crear_orden_venta, name="crear_orden_venta"),
    path("borrar_orden/<int:orden_id>/", borrar_orden, name="borrar_orden"),
    # Otras rutas...
]
