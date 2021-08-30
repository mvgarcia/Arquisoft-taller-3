from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_id, delete_measurement_id
from django.http import HttpResponse
from django.core import serializers
from .models import Measurement
from .forms import MeasurementForm
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

def save_measurement_form(request, form):
    if request.method == 'POST':
        if form.is_valid():
            form.save()

def update_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = get_object_or_404(Measurement, pk=pk)
    else:
        form = MeasurementForm()

    return render(request, 'update.html', {'form': form})

"""def update_measurement(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MeasurementForm()

    return render(request, 'update.html', {'form': form})"""
