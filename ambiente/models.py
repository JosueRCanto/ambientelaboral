from django.db import models

# Create your models here.

class Resultados (models.Model):
    area=models.CharField(max_length=30)
    condiciones=models.IntegerField()
    cooperacion=models.IntegerField()
    supervision=models.IntegerField()
    condicionesfisicas=models.IntegerField()
    satisfaccion=models.IntegerField()
    participacion=models.IntegerField()
