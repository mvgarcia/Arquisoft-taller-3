from django import forms
from .models import Measurement

class MeasurementForm(forms.Form):
    value = forms.FloatField(label='New value')
    unit = forms.CharField(label='New unit',max_length=50)
    place = forms.CharField(label='New place',max_length=50)