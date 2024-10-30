from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Trabajador, Departamento, Area, CargaFamiliar
from .forms import TrabajadorForm, DepartamentoForm, AreaForm, CargaFamiliarForm

# Trabajador
class TrabajadorListView(ListView):
    model = Trabajador
    template_name = 'trabajador_list.html'
    context_object_name = 'trabajadores'

class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')

class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'trabajador_confirm_delete.html'
    success_url = reverse_lazy('trabajador_list')

# Departamento
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento_list.html'
    context_object_name = 'departamentos'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento_form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento_form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento_list')

# Area
class AreaListView(ListView):
    model = Area
    template_name = 'area_list.html'
    context_object_name = 'areas'

class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'area_form.html'
    success_url = reverse_lazy('area_list')

class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'area_form.html'
    success_url = reverse_lazy('area_list')

class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'area_confirm_delete.html'
    success_url = reverse_lazy('area_list')

# CargaFamiliar
class CargaFamiliarListView(ListView):
    model = CargaFamiliar
    template_name = 'carga_familiar_list.html'
    context_object_name = 'cargas_familiares'

class CargaFamiliarCreateView(CreateView):
    model = CargaFamiliar
    form_class = CargaFamiliarForm
    template_name = 'carga_familiar_form.html'
    success_url = reverse_lazy('carga_familiar_list')

class CargaFamiliarUpdateView(UpdateView):
    model = CargaFamiliar
    form_class = CargaFamiliarForm
    template_name = 'carga_familiar_form.html'
    success_url = reverse_lazy('carga_familiar_list')

class CargaFamiliarDeleteView(DeleteView):
    model = CargaFamiliar
    template_name = 'carga_familiar_confirm_delete.html'
    success_url = reverse_lazy('carga_familiar_list')

