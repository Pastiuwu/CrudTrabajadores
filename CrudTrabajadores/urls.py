from django.urls import path
from . import views

urlpatterns = [
    # Trabajador
    path('trabajadores/', views.TrabajadorListView.as_view(), name='trabajador_list'),
    path('trabajadores/crear/', views.TrabajadorCreateView.as_view(), name='trabajador_create'),
    path('trabajadores/<int:pk>/editar/', views.TrabajadorUpdateView.as_view(), name='trabajador_edit'),
    path('trabajadores/<int:pk>/eliminar/', views.TrabajadorDeleteView.as_view(), name='trabajador_delete'),
    
    # Departamento
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/crear/', views.DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:pk>/editar/', views.DepartamentoUpdateView.as_view(), name='departamento_edit'),
    path('departamentos/<int:pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name='departamento_delete'),
    
    # Area
    path('areas/', views.AreaListView.as_view(), name='area_list'),
    path('areas/crear/', views.AreaCreateView.as_view(), name='area_create'),
    path('areas/<int:pk>/editar/', views.AreaUpdateView.as_view(), name='area_edit'),
    path('areas/<int:pk>/eliminar/', views.AreaDeleteView.as_view(), name='area_delete'),
    
    # CargaFamiliar
    path('cargas_familiares/', views.CargaFamiliarListView.as_view(), name='carga_familiar_list'),
    path('cargas_familiares/crear/', views.CargaFamiliarCreateView.as_view(), name='carga_familiar_create'),
    path('cargas_familiares/<int:pk>/editar/', views.CargaFamiliarUpdateView.as_view(), name='carga_familiar_edit'),
    path('cargas_familiares/<int:pk>/eliminar/', views.CargaFamiliarDeleteView.as_view(), name='carga_familiar_delete'),
]
