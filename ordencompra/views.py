from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import TuModelo
import openpyxl

# Create your views here.


def ordencompra(request):
    return HttpResponse("Hola mundo")


def importar_datos(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES["archivo"]
            workbook = openpyxl.load_workbook(archivo)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                # Suponiendo que el archivo Excel tiene dos columnas, ajusta según tus necesidades
                TuModelo.objects.create(campo1=row[0], campo2=row[1])

            mensaje_exito = "¡Importación exitosa!"
            return render(request, "ordencompra.html", {"mensaje_exito": mensaje_exito})
    else:
        form = UploadFileForm()

    return render(request, "importar_datos.html", {"form": form})
