
# Dada la siguiente clase
#
class Vehiculo(models.Model):
    placa = models.CharField(max_length=30)

    def __str__(self):
        return "Placa: %s" % (self.placa) 

# Se ha agregado los siguiente objetos
#

Placa: lcc0099
Placa: gap0909

# Cuál de las siguientes opciones permite seleccionar los 
# registros que tengan la secuencia 099
#
# Opción a
Vehiculo.objects.filter(placa_contains="099") 

# Opción b
Vehiculo.objects.filter(placa__contains="099") 


# Opción c
Vehiculo.objects.filter(placa.contains="099") 
