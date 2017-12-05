from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Carros(models.Model):
    Placas = models.CharField(max_length=50, blank = False)
    Serie = models.CharField(max_length=50, blank=False)
    Motor = models.CharField(max_length=50, blank=False)
    Marca = models.CharField(max_length=30, blank=False)
    Modelo = models.DecimalField(max_digits=1000, decimal_places=0, null=True, blank=True)
    Tipo_vehiculo = models.CharField(max_length=30, blank=False)
    Ano = models.DecimalField(max_digits=1000, decimal_places=0, null=True, blank=True)
    Color = models.CharField(max_length=30, blank=False)
    slug = models.SlugField(blank=True)

    def __unicode_(self):
        return self.Serie

def Carros_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.Placas)

pre_save.connect(Carros_pre_save_reciever, sender=Carros)
