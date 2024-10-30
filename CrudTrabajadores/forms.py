from django import forms
from .models import Trabajador, Departamento, Area, CargaFamiliar

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

class CargaFamiliarForm(forms.ModelForm):
    class Meta:
        model = CargaFamiliar
        fields = '__all__'
