from django.db import models

# Create your models here.

class Model_MEDIO(models.Model):

    medio_detalle = models.CharField(max_length=150,verbose_name="Medio Detalle")

    class Meta:

        managed = True
        db_table = 'model_medio'
        verbose_name= "MODEL_MEDIO"
        verbose_name_plural = "MODEL_MEDIOS" 
        ordering = ['id']   

    def __str__(self):

        return  self.medio_detalle

class Model_RED(models.Model):

    red_detalle = models.CharField(max_length=150,verbose_name="Medio Detalle")

    class Meta:

        managed = True
        db_table = 'model_red'
        verbose_name= "MODEL_RED"
        verbose_name_plural = "MODEL_REDS" 
        ordering = ['id']   
          

    def __str__(self):

        return self.red_detalle

class Model_OIT(models.Model):

    oit =  models.CharField(max_length=20, verbose_name="ID OIT")
    servicio = models.TextField(verbose_name="Servicio")
    medio = models.ForeignKey(Model_MEDIO, on_delete=models.CASCADE)
    red = models.ForeignKey(Model_RED, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=150,verbose_name="Proveedor")
    fecha_acordada = models.DateField(verbose_name="Fecha Acordada")
    plazo_contrato = models.DateField(verbose_name="Plazo Contrato")
    renta_mensual = models.CharField(max_length=150,verbose_name="Renta Mensual")
    proceso = models.CharField(max_length=150,verbose_name="Proceso")
    mes_venta = models.DateField(verbose_name="Mes Venta")
    

    class Meta:

        managed = True
        db_table = 'model_oit'
        verbose_name= "MODEL_OIT"
        verbose_name_plural = "MODEL_OITs"    

    def __str__(self):

        return "%s %s" % (self.oit, self.servicio)

