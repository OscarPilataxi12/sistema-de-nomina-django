from django import forms
from .models import Empleado
from .models import Nomina, NominaDetalle

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cedula', 'nombre', 'sueldo', 'departamento', 'cargo']

class NominaForm(forms.ModelForm):
    class Meta:
        model = Nomina
        fields = ['aniomes']

class NominaDetalleForm(forms.ModelForm):
    class Meta:
        model = NominaDetalle
        fields = ['empleado', 'sueldo', 'bono', 'prestamo']