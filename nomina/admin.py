from django.contrib import admin
from .models import Empleado, Nomina, NominaDetalle

admin.site.register(Empleado)
admin.site.register(Nomina)
admin.site.register(NominaDetalle)
