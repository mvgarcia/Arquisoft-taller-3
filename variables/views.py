from django.shortcuts import render
from .logic.logic_variables import get_all_variables
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def get_variables(request):
    variables = get_all_variables()
    variable_list = serializers.serialize('json',variables)
    return HttpResponse(variable_list, content_type='application/json')
