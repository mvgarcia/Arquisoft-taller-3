from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_id, delete_measurement_id
from django.http import HttpResponse
from django.core import serializers
from .models import Measurement
from .forms import MeasurementForm
import json
from django.shortcuts import get_object_or_404
#from rest_framework.decorators import api_view

# Create your views here.

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

#@api_view(['GET', 'PUT', 'DELETE'])
def get_measurement(request, id=None):
    measurement = get_measurement_id(id=id)
    return HttpResponse(measurement, content_type='application/json')

def delete_measurement(request, id=None):
    mensage = delete_measurement_id(id=id)
    return HttpResponse(mensage)

"""def save_measurement_form(request, form):
    if request.method == 'POST':
        if form.is_valid():
            form.save()"""

"""def update_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = get_object_or_404(Measurement, pk=pk)
    else:
        form = MeasurementForm()

    return render(request, 'update.html', {'form': form})"""

def prueba(request,id):
    if request.method == 'PUT':
        measurement = get_object_or_404(Measurement,pk=id)
        print(measurement.value)
        measurement_body = json.loads(request.body)
        measurement.value = measurement_body['value']
        measurement.save()

        return HttpResponse(measurement, content_type='application/json')
