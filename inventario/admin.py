from django.contrib import admin

# Register your models here.

from .models import Inventory
from import_export.admin import ImportExportModelAdmin


admin.site.register(Inventory, ImportExportModelAdmin)
