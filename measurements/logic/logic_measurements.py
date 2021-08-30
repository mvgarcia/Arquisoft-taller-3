from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_id(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement
def delete_measurement_id(id):
    measurement = Measurement.objects.get(pk=id).delete()
    return ("Medida eliminada")

