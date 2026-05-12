from django.db import models
from django.contrib.auth.models import User

class Evaluacion(models.Model):
    nino = models.ForeignKey('ninos.Nino', on_delete=models.CASCADE)
    evaluador = models.ForeignKey(User, on_delete=models.CASCADE)

    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    talla = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField(blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Evaluación {self.nino} - {self.fecha}"
