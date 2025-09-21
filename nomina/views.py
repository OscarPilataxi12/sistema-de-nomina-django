from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from .models import Nomina, NominaDetalle
from .forms import NominaForm, NominaDetalleForm
from django.db.models import Sum
from django.utils.timezone import now

# Listar empleados
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'nomina/lista_empleados.html', {'empleados': empleados})

# Crear empleado
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'nomina/empleado_form.html', {'form': form})

# Editar empleado
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'nomina/empleado_form.html', {'form': form})

# Eliminar empleado
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'nomina/confirmar_eliminar.html', {'empleado': empleado})

# Listar Nóminas
def lista_nominas(request):
    nominas = Nomina.objects.all()
    return render(request, 'nomina/lista_nominas.html', {'nominas': nominas})

# Crear Nómina
def crear_nomina(request):
    if request.method == 'POST':
        form = NominaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_nominas')
    else:
        form = NominaForm()
    return render(request, 'nomina/nomina_form.html', {'form': form})

# Editar Nómina
def editar_nomina(request, pk):
    nomina = get_object_or_404(Nomina, pk=pk)
    if request.method == 'POST':
        form = NominaForm(request.POST, instance=nomina)
        if form.is_valid():
            form.save()
            return redirect('lista_nominas')
    else:
        form = NominaForm(instance=nomina)
    return render(request, 'nomina/nomina_form.html', {'form': form})

# Eliminar Nómina
def eliminar_nomina(request, pk):
    nomina = get_object_or_404(Nomina, pk=pk)
    if request.method == 'POST':
        nomina.delete()
        return redirect('lista_nominas')
    return render(request, 'nomina/confirmar_eliminar_nomina.html', {'nomina': nomina})

# Listar Detalles de una Nómina
def detalles_nomina(request, pk):
    nomina = get_object_or_404(Nomina, pk=pk)
    detalles = NominaDetalle.objects.filter(nomina=nomina)
    return render(request, 'nomina/detalles_nomina.html', {'nomina': nomina, 'detalles': detalles})

# Agregar Detalle a la Nómina
def agregar_detalle_nomina(request, pk):
    nomina = get_object_or_404(Nomina, pk=pk)
    if request.method == 'POST':
        form = NominaDetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.nomina = nomina
            detalle.save()

            # recalcular totales
            totales = NominaDetalle.objects.filter(nomina=nomina)
            nomina.tot_ing = sum([d.tot_ing for d in totales])
            nomina.tot_des = sum([d.tot_des for d in totales])
            nomina.neto = sum([d.neto for d in totales])
            nomina.save()

            return redirect('detalles_nomina', pk=nomina.pk)
    else:
        form = NominaDetalleForm()
    return render(request, 'nomina/detalle_form.html', {'form': form, 'nomina': nomina})

def dashboard(request):
    empleados = Empleado.objects.count()
    ultima_nomina = Nomina.objects.order_by('-aniomes').first()
    detalles = None

    if ultima_nomina:
        detalles = NominaDetalle.objects.filter(nomina=ultima_nomina)

    contexto = {
        'empleados': empleados,
        'ultima_nomina': ultima_nomina,
        'detalles': detalles,
    }
    return render(request, 'nomina/dashboard.html', contexto)