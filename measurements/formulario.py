from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Measurement

class Formulario(forms.ModelForm):

    class Meta:
        model= Measurement
        fields= '__all__'
        