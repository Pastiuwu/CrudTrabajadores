from django.db import models
from django.core.exceptions import ValidationError

#def validate_active_status(value):
#    if not isinstance(value, bool):
#        raise ValidationError("BORRAR VALIDACION XD")

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    fecha_ingreso = models.DateField()
    estado_activo = models.BooleanField(default=True, validators=[validate_active_status])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=50, blank=False)
    ubicacion = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nombre_departamento

class Area(models.Model):
    TIPO_AREA_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Finanzas', 'Finanzas'),
        ('Logistica', 'Logística'),
        ('IT', 'IT'),
        ('Ventas', 'Ventas'),
        ('Administrativa', 'Administrativa'),
    ]
    nombre_area = models.CharField(max_length=50, blank=False)
    tipo_area = models.CharField(max_length=50, choices=TIPO_AREA_CHOICES, blank=False)

    def __str__(self):
        return self.nombre_area

class CargaFamiliar(models.Model):
    nombre_carga = models.CharField(max_length=50, blank=False)
    relacion = models.CharField(max_length=50, blank=False)
    GRUPO_SALUD_CHOICES = [
        ('Fonasa', 'Fonasa'),
        ('Isapre', 'Isapre'),
    ]
    grupo_salud = models.CharField(max_length=50, choices=GRUPO_SALUD_CHOICES, blank=False)

    def __str__(self):
        return self.nombre_carga

