# forms.py

from .models import OrdenDeVenta, ItemOfertaDeVenta
from django import forms


class InventarioUploadForm(forms.Form):
    archivo_excel = forms.FileField()


class ExcelUploadForm(forms.Form):
    archivo_excel = forms.FileField()


class OrdenDeVentaForm(forms.ModelForm):
    class Meta:
        model = OrdenDeVenta
        fields = [
            "codigo_sap",
            "nombre_proyecto",
            "direccion_proyecto",
            "fecha",
            "observacion",
        ]


class ItemOfertaDeVentaForm(forms.ModelForm):
    class Meta:
        model = ItemOfertaDeVenta
        fields = ["numero_oferta", "nombre", "precio", "cantidad"]
