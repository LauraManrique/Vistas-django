from ..models import Measurement

def get_all_measurements():
    measurements= Measurement.objects.all()
    return measurements

def get_measurement_pk(llave):
    one_measurement = Measurement.objects.get(pk=llave)
    return one_measurement