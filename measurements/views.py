from measurements.formulario import Formulario
from django.shortcuts import render


# Create your views here.
from .logic.logic_measurements import get_all_measurements, get_measurement_pk
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements= get_all_measurements()
    measurement_list= serializers.serialize('json', measurements)
    return HttpResponse(measurement_list,content_type= 'application/json')

def get_measurement(request, llave):
    measurement= get_measurement_pk(llave)
    measurement_one= serializers.serialize('json', [measurement,])
    return HttpResponse(measurement_one,content_type= 'application/json')


def edit(request, id_medida):
    medida= get_measurement_pk(id_medida)
    form= Formulario(instance=medida)
    return render(request, "MedidaEdit.html", {"form":form, 'medida': medida})

def actualizarMedida(request, id_medida):
    medida= get_measurement_pk(id_medida)
    form= Formulario(request.POST, instance=medida)
    if form.is_valid():
        form.save()
    actualizado= get_measurement(request, id_medida)   
    return actualizado

def eliminar(request, id_medida):
    medida= get_measurement_pk(id_medida)
    medida.delete()
    html= '<html><body> "Eliminado exitosamente"  </body> <html '
    return HttpResponse(html)