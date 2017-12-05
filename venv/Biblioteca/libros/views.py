from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q
from biblioteca.multipleslug import MultiSlugMixin
from .models import Carros
from .forms import CarrosAddForm, CarrosModelForm
import os
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import CarrosAddForm, CarrosModelForm
from .models import Carros
from django.conf import settings
from mimetypes import guess_type
from wsgiref.util import FileWrapper
from django.views.generic.detail import DetailView


# Create your views here.

def home(request):

    context=locals()
    template='index0.html'
    return render(request,template,context)

class ActualizarCarros(UpdateView):
    model = Carros
    form_class = CarrosModelForm
    success_url = "/carros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarCarros, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Actualizar"
        return context

class DetalleDeCarros(MultiSlugMixin,DetailView):
    model = Carros

class ListaDeCarros(ListView):
    model = Carros

    def get_queryset(self, *args, **kwargs):
        consulta = super(ListaDeCarros, self).get_queryset(**kwargs)
        query = self.request.GET.get("q",'')
        consulta =consulta.filter(
                      Q(Placas__icontains=query)).order_by("Placas")
        print query
        return consulta


class CrearCarros(CreateView):
    model = Carros
    form_class = CarrosModelForm
    success_url = "/carros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(CrearCarros, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Registrar"
        return context

def lista_Carros(request):
    lib = Carros.objects.all()
    print request
    mens = "Carros Registrados Actualmente"
    template = "listaDeCarros.html"
    contexto= {"Mensaje": mens,
               "Carros": lib }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        Carros = get_object_or_404(Carros, slug=slug)
    except Carros.MultipleObjectsReturned:
        Carros = Carros.objects.filter(slug=slug).order_by("-Placas").first()

    print Carros
    mens = "Carros nuevos"
    template = "detalle_slug.html"
    contexto= {"mensaje":mens,
           "Carros": Carros }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    #Logico de negocio alias hechizo
    try:
        Carros = get_object_or_404(Producto, slug=slug)
    except Carros.MultipleObjectsReturned:
        Carros = Carros.objects.filter(slug=slug).order_by("-Placas").first()
    mens = "Carros nuevos"
    template = "detalle_slug.html"
    contexto= {"mensaje":mens,
           "Carros": Carros }
    return render(request, template, contexto)

def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    Carros = get_object_or_404(Carros, id=object_id)
    form = CarrosModelForm(request.POST or None, instance=Carros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "Carros": Carros,
           "form":form,
           "titulo":"Actualizar Carros"
           }
    return render(request, template, contexto)

def detalle_Carros(request, object_id=None):

    lib = get_object_or_404(Carros, id=object_id)
    mens = "Carros Registrados Actualmente"
    template = "detalle_Carros.html"
    contexto= {"Mensaje":mens,
           "Carros": lib }
    return render(request, template, contexto)


def agregar_Carros(request):
    form = CarrosAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta hecha"
    #if request.method == "POST":
    #    print request.POST
    #if form.is_valid():
    #    data = form.cleaned_data
    #    nombre = data.get("nombre")
    #    autor = data.get("autor")
    #    editorial= data.get("editorial")
    #    isbn= data.get("isbn")
    #    precio= data.get("precio")

    #    nuevo_Carros = Carros()
    #    nuevo_Carros.Nombre = nombre
    #    nuevo_Carros.Autor = autor
    #    nuevo_Carros.Editorial = editorial
    #    nuevo_Carros.ISBN = isbn
    #    nuevo_Carros.Precio = precio
    #    nuevo_Carros.save()

    template = "agregar_Carros.html"

    context = {
    "titulo":"Crear Producto",
    "form":form
    }

    return render(request, template, context)
