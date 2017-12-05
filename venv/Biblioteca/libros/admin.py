from __future__ import unicode_literals
from django.contrib import admin
from libros.models import Carros
# Register your models here.

class CarrosAdmin(admin.ModelAdmin):
    list_display = ("id","Placas", "Serie", "Motor", "Marca", "Modelo", "Tipo_vehiculo", "Ano", "Color")
    search_fields = ["Placas"]
    list_editable = ["Motor"]
    list_filter = ["Serie"]
    class meta:
        model = Carros

admin.site.register(Carros,CarrosAdmin)
