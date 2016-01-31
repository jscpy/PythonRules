from django.contrib import admin

from empresa.models import Empleado, Departamento

admin.site.register(Empleado)
admin.site.register(Departamento)
