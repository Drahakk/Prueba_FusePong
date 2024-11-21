from django.db import models


# Create your models here.


class D(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    estado = models.CharField(max_length=100, verbose_name='Estado')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

class T(models.Model):
    #D = models.ForeignKey(D, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    tituloticket = models.CharField(max_length=100, verbose_name='Titulo')
    descripcionticket = models.TextField(blank=True, verbose_name='Descripción')
    estadoticket = models.CharField(max_length=100, verbose_name='Estado')

    def __str__(self):
        fila = "Titulo: " + self.tituloticket + " - " + "Descripción: " + self.descripcionticket
        return fila
