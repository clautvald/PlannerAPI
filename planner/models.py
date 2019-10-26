from django.db import models

# Create your models here.
class Evento(models.Model): 
    eventos_nombre= models.CharField(max_length =150)
    
    def __str__(self):
        return self.eventos_nombre

class Servicio(models.Model): 
    servicios_nombre = models.CharField(max_length =150)
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.servicios_nombre

class Producto(models.Model):
    nombre_producto = models.CharField(max_length =150)
    caracteristicas = models.CharField(max_length =150)
    precio = models.IntegerField(default =0)

class Proveedore(models.Model): 
    proveedores_nombre = models.CharField(max_length =150)
    direccion = models.CharField(max_length =150)
    contacto_nombre = models.CharField(max_length = 150)
    celular = models.IntegerField(default =0)
    correo = models.CharField(max_length =150)
    
    servicios = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos= models.ForeignKey(Producto, on_delete=models.CASCADE)
    def __str__(self):
        return self.proveedores_nombre


    
class Cliente(models.Model): 
    nombre_cliente = models.CharField(max_length =150)
    apellidos_cliente = models.CharField(max_length =150)
    celular_cliente = models.CharField(max_length =150)
    correo_cliente = models.CharField(max_length =150)
    genero = models.CharField(max_length =150)
    edad = models.IntegerField(default =0)
    
    def __str__(self):
        return self.nombre_cliente
        
class MiEvento(models.Model):
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)
    servicios = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos= models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedores = models.ForeignKey(Proveedore, on_delete=models.CASCADE)
    productos= models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_evento = models.DateTimeField('fecha de evento')

