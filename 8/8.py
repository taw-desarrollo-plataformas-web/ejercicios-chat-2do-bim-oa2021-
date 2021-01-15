from django.db import models

# Opción A
class Vehiculo(models.Model):
    placa = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.placa) 


# Opción B
class Vehiculo(models):
    placa = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.placa) 


# Opción C
class Vehiculo(Model):
    placa = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.placa) 


