from django.db import models

class Nino(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)

    latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

    estado_nutricional_actual = models.CharField(max_length=50, blank=True)

    tutor = models.OneToOneField('tutores.Tutor', on_delete=models.CASCADE)
    comunidad = models.ForeignKey('comunidades.Comunidad', on_delete=models.CASCADE)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    estado_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"