from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class Empleado(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Nomina(models.Model):
    aniomes = models.CharField(max_length=6)  # formato: 202401
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Nómina {self.aniomes}"


class NominaDetalle(models.Model):
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    bono = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iess = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prestamo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # calcular totales antes de guardar
        self.tot_ing = self.sueldo + self.bono
        self.iess = (self.sueldo * Decimal("0.0945")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.tot_des = self.iess + self.prestamo
        self.neto = self.tot_ing - self.tot_des
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.nomina.aniomes}"
