from django.contrib import admin

# Register your models here.

from . models import Inventario
from import_export.admin import ImportExportModelAdmin


admin.site.register(Inventario, ImportExportModelAdmin)