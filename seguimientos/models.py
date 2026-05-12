from django.db import models

class Seguimiento(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Graduado', 'Graduado'),
        ('Abandono', 'Abandono'),
    ]

    nino = models.ForeignKey('ninos.Nino', on_delete=models.CASCADE)

    fecha_proximo_control = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Seguimiento {self.nino}"
    