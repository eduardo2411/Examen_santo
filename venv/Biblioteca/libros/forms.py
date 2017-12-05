from django import forms
from .models import Carros

OPCIONES_TIPO = (
    ('ya no mas ', "ya no mas"),
    ('editorial bajo el techo', "Editorial bajo el techo"),
    ('semestre zero', "semestre zero"),
)

class CarrosAddForm(forms.Form):
    Placas=forms.CharField(label="Nombre del Carros",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca el numero de Placas'}))

    Serie=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    Motor=forms.ChoiceField(choices=OPCIONES_TIPO)
    Marca=forms.CharField()
    Modelo=forms.DecimalField()
    Tipo_vehiculo=forms.CharField()
    ano=forms.DecimalField()
    Color=forms.CharField()

    def clean_precio(self):
        precio=self.cleaned_data.get("precio")
        if precio <=200.00:
            raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
        elif precio >=19999.99:
            raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
        else:
            return precio



class CarrosModelForm(forms.ModelForm):
    #Editorial = forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model = Carros
        fields =[
            "Placas",
            "Serie",
            "Motor",
            "Marca",
            "Modelo",
            "Tipo_vehiculo",
            "Ano",
            "Color",
        ]
        labels = {
            "Placas": "Cual es el numero de placas del vehiculo",
            "Series":"Cual es el numero de Serie del vehiculo",
            "Motor":"Cual es la numeracion del Motor",
            "Marca":"Cual es la marca del vehiculo",
            "Modelo":"Cual es el modelo del Vehiculos",
            "Tipo_vehiculo":"Que tipo de vehiculo es",
            "Ano": "Cual es el ano del vehiculo",
            "Color":"Cual es el color del vehiculo"
        }
        widgets = {
            "Placas": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el numero de placas'}),
            "Serie": forms.TextInput(attrs={'class': 'form-control'}),
            "Motor": forms.TextInput(attrs={'class': 'form-control'}),
            "Marca":forms.TextInput(attrs={'class':'form-control'}),
            "Modelos":forms.TextInput(attrs={'class':'form-control'}),
            "Tipo_vehiculo":forms.TextInput(attrs={'class':'form-control'}),
            "Ano":forms.NumberInput(attrs={'class':'form-control'}),
            "Color":forms.TextInput(attrs={'class':'form-control'}),
        }

    #def clean_precio(self):
        # precio=self.cleaned_data.get("precio")
        # if precio <=200.00:
        #     raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
        # elif precio >=19999.99:
        #     raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
        # else:
        #     return precio
